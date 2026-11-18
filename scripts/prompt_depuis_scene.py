"""Génère le prompt d'un plan à partir de la GÉOMÉTRIE MESURÉE dans Blender.

Principe : ce que la scène sait, le prompt ne doit pas le réinventer. Focale,
distance, échelle, sens écran, entrée/sortie de champ, mouvement de caméra,
profondeur du fond et lumière sont MESURÉS image par image, puis traduits en
consignes. Un prompt écrit ainsi ne peut pas contredire la scène.

Structure du prompt, toujours dans cet ordre (voir FLOW.md) :
    REFERENCES -> FRAME -> MOVEMENT -> CONTINUITY -> DO NOT

    exec(open('.../scripts/prompt_depuis_scene.py').read())
    fiche = mesurer("CAM_P04B_carrefour_200")
    ecrire_prompt("P04B", fiche, intention=..., refs=..., continuite=...)
"""
import bpy
import math
import os
from mathutils import Vector
from bpy_extras.object_utils import world_to_camera_view

BASE = "./KIMKATCHER/EP01/"
CAPTEUR_H = 36.0 / 2.39          # 15,06 mm en 2.39:1
TAILLE = 1.78


def _echelle(hauteur_champ):
    """Nom de la valeur de plan d'après la hauteur de champ au niveau du sujet."""
    r = hauteur_champ / TAILLE
    if r > 2.2:
        return "wide shot, full figure small in frame"
    if r > 1.05:
        return "full-length shot, head to toe"
    if r > 0.75:
        return "medium-long shot, cut at the knees"
    if r > 0.5:
        return "medium shot, cut at the waist"
    if r > 0.3:
        return "medium close-up, head and shoulders"
    return "close-up on the face"


def _angle(vue, orientation):
    """Angle de prise de vue sur le sujet, d'après vue . orientation."""
    d = vue.dot(orientation)
    if d < -0.8:
        return "facing the camera"
    if d < -0.3:
        return "three-quarter front view"
    if d < 0.3:
        return "clean profile"
    if d < 0.8:
        return "three-quarter back view"
    return "seen from behind"


def mesurer(nom_cam, sujet="KIM_racine", orientation=Vector((-1, 0, 0))):
    scene = bpy.context.scene
    cam = bpy.data.objects[nom_cam]
    kim = bpy.data.objects[sujet]
    n0, n1 = scene.frame_start, scene.frame_end
    fps = scene.render.fps

    xs, dists, focales, positions, visees, dans = [], [], [], [], [], []
    for f in range(n0, n1 + 1):
        scene.frame_set(f)
        bpy.context.view_layer.update()
        k = Vector(kim.matrix_world.translation)
        c = Vector(cam.matrix_world.translation)
        co = world_to_camera_view(scene, cam, k + Vector((0, 0, 0.9)))
        xs.append(co.x)
        dans.append(0.0 <= co.x <= 1.0 and co.z > 0)
        dists.append((k - c).length)
        focales.append(cam.data.lens)
        positions.append(c)
        visees.append((cam.matrix_world.to_quaternion() @ Vector((0, 0, -1))).normalized())

    idx_in = [i for i, v in enumerate(dans) if v]
    entree = idx_in[0] if idx_in else None
    sortie = idx_in[-1] if idx_in else None

    # Sens écran : sur les images où il est visible
    sens = None
    if idx_in and len(idx_in) > 4:
        dx = xs[idx_in[-1]] - xs[idx_in[0]]
        # Si la caméra le suit, il reste centré : on lit le sens dans le pano
        if abs(dx) < 0.08:
            rot = visees[idx_in[0]].cross(visees[idx_in[-1]]).z
            sens = "left to right" if rot < 0 else "right to left"
        else:
            sens = "left to right" if dx > 0 else "right to left"

    trajet_cam = (positions[-1] - positions[0]).length
    pano = math.degrees(visees[0].angle(visees[-1]))
    zoom = (focales[0], focales[-1])

    # Fin de plan : angle, échelle, fond, lumière
    scene.frame_set(n1)
    bpy.context.view_layer.update()
    k = Vector(kim.matrix_world.translation) + Vector((0, 0, 1.2))
    c = Vector(cam.matrix_world.translation)
    vue = (k - c).normalized()
    angle = _angle(vue, orientation)
    h_fin = CAPTEUR_H / focales[-1] * dists[-1]

    dg = bpy.context.evaluated_depsgraph_get()
    ok, loc, _, _, obj, _ = scene.ray_cast(dg, k + vue * 0.6, vue)
    fond = (loc - k).length if ok else 999.0

    lumiere = None
    soleil = bpy.data.objects.get("Soleil_Avril")
    if soleil:
        dir_lum = (soleil.matrix_world.to_quaternion() @ Vector((0, 0, -1))).normalized()
        lumiere = vue.dot(dir_lum)     # < 0 : contre-jour (voir ecrire_prompt)

    return {
        "camera": nom_cam, "fps": fps, "images": n1 - n0 + 1,
        "duree": (n1 - n0 + 1) / fps,
        "focale_debut": zoom[0], "focale_fin": zoom[1],
        "dist_min": min(dists), "dist_max": max(dists), "dist_fin": dists[-1],
        "echelle_fin": _echelle(h_fin), "hauteur_champ_fin": h_fin,
        "angle_fin": angle,
        "entree_s": None if entree is None else entree / fps,
        "sortie_s": None if sortie is None else sortie / fps,
        "visible_debut": dans[0], "visible_fin": dans[-1],
        "sens": sens, "trajet_camera_m": trajet_cam, "pano_deg": pano,
        "fond_m": fond, "contre_jour": lumiere,
    }


def _mouvement_camera(m):
    if abs(m["focale_fin"] - m["focale_debut"]) > 5:
        return (f"The camera does not move in space. It performs an optical zoom from "
                f"{m['focale_debut']:.0f} mm to {m['focale_fin']:.0f} mm: the perspective "
                f"never changes, only the frame tightens.")
    if m["trajet_camera_m"] < 0.3 and m["pano_deg"] < 3:
        return ("Locked-off tripod shot. The camera does not move at all: no pan, no tilt, "
                "no push-in, no zoom, no handheld shake.")
    if m["trajet_camera_m"] < 0.3:
        return (f"The camera stays in place on a tripod and PANS {m['sens']} by about "
                f"{m['pano_deg']:.0f} degrees, following him. It never travels.")
    return (f"The camera travels about {m['trajet_camera_m']:.0f} m alongside him, "
            f"keeping a steady distance.")


def ecrire_prompt(plan, m, intention, refs, continuite, interdits_plan=(), sauver=True):
    fr = []
    fr.append(f"# {plan} — généré depuis la scène Blender ({m['camera']})")
    fr.append(f"# Mesures : {m['duree']:.1f} s | {m['focale_debut']:.0f}"
              + (f"->{m['focale_fin']:.0f}" if abs(m['focale_fin'] - m['focale_debut']) > 5 else "")
              + f" mm | distance {m['dist_min']:.1f}-{m['dist_max']:.1f} m | "
              f"hauteur de champ {m['hauteur_champ_fin']:.2f} m | fond à "
              + ("plus de 70 m" if m["fond_m"] > 70 else f"{m['fond_m']:.0f} m"))
    fr.append("")

    en = []
    en.append("REFERENCES")
    # Un rendu en blocs gris se lit mal : les piétons-boîtes passent pour des
    # immeubles, et Runway a pris le cadrage du plan 6 pour « une ville vue d'en
    # haut » (2026-09-29). On le dit explicitement à chaque fois.
    en.append("- Any grey 3D blockout reference is NOT a photo: its tall grey boxes are "
              "PEOPLE, not buildings; the figure with a head is the young man; the camera "
              "is at eye level. Use it only for framing, angle, subject size and position.")
    for tag, role in refs:
        en.append(f"- @{tag}: {role}")
    en.append("")

    en.append("FRAME")
    en.append(f"Shot on a {m['focale_fin']:.0f}mm lens from {m['dist_fin']:.0f} metres away, "
              f"{m['echelle_fin']}, {m['angle_fin']}.")
    if m["focale_fin"] >= 150:
        en.append("Telephoto compression: the crowd is stacked in flat layers with no "
                  "vanishing point. He is sharp; everyone else is soft.")
    if m["fond_m"] > 40:
        en.append("Behind him the street opens deep into the distance: a bright band of "
                  "sunlit ground and pale sky, against which his dark silhouette stands out.")
    else:
        en.append("Behind him, a stone facade close by, softly out of focus.")
    # contre_jour = vue . direction de propagation de la lumière.
    # NÉGATIF : la lumière voyage vers la caméra -> elle vient de derrière lui.
    # (Signe inversé dans la première version : corrigé le 2026-09-29.)
    if m["contre_jour"] is not None:
        if m["contre_jour"] < -0.2:
            en.append("He is BACKLIT: the sun is behind him, rimming his hair and shoulders "
                      "with a thin edge of light; his front is in soft shadow.")
        elif m["contre_jour"] > 0.2:
            en.append("The sun is behind the camera and lights him from the front.")
        else:
            en.append("Side light: one side of his face lit, the other in shadow.")
    en.append("Manhattan, midday, early April. Cool grey, stone and pale blue palette. "
              "2.39:1 anamorphic, natural light, no colour grade.")
    en.append("")

    en.append("MOVEMENT")
    en.append(intention)
    if m["entree_s"] is not None and not m["visible_debut"]:
        en.append(f"He is OUT OF FRAME at the start and ENTERS the frame at about "
                  f"{m['entree_s']:.1f} s, moving {m['sens']}.")
    elif m["sens"]:
        en.append(f"He moves {m['sens']} across the frame.")
    if m["visible_debut"] and not m["visible_fin"] and m["sortie_s"] is not None:
        en.append(f"He LEAVES the frame at about {m['sortie_s']:.1f} s; the camera lets him go.")
    en.append(_mouvement_camera(m))
    en.append(f"Duration {m['duree']:.0f} s, real-time speed.")
    en.append("")

    en.append("CONTINUITY")
    en.append(continuite)
    en.append("Keep his face, hair and clothing identical to the references throughout. "
              "No morphing, no identity drift.")
    en.append("")

    base = ["slow motion", "speed ramp", "text overlay", "watermark", "added music",
            "lens flare", "colour grading", "night", "sunset light", "green park foliage",
            "mask", "glowing tattoo", "red glow on skin"]
    if m["trajet_camera_m"] < 0.3 and abs(m["focale_fin"] - m["focale_debut"]) < 5:
        base += ["zoom", "dolly", "push-in"]
    if m["sens"] == "left to right":
        base += ["walking toward the left", "walking toward the camera"]
    en.append("DO NOT: " + ", ".join(list(interdits_plan) + base) + ".")
    en.append("")
    en.append("SETTINGS: Seedance 2.5, 21:9, "
              f"{max(5, round(m['duree']))}s, 720p, native audio OFF.")

    texte = "\n".join(fr + ["```"] + en + ["```"]) + "\n"
    if sauver:
        import glob
        cands = [c for c in glob.glob(os.path.join(BASE, "PLANS", f"{plan}_*"))
                 if os.path.basename(c).split("_")[0] == plan]
        dossier = os.path.join(cands[0], "2_A_ENVOYER") if cands else os.path.join(BASE, "_travail")
        os.makedirs(dossier, exist_ok=True)
        chemin = os.path.join(dossier, "PROMPT_genere.txt")
        with open(chemin, "w", encoding="utf-8") as fh:
            fh.write(texte)
        return chemin, texte
    return None, texte


def verifier_premier_plan(nom_cam, seuil_m=None, grille=(13, 7)):
    """Balaye le cadre par une grille de rayons et renvoie les objets situés
    ENTRE la caméra et le sujet (premier plan parasite).

    À appeler AVANT ecrire_prompt : une image de contrôle qui montre un
    premier plan que le prompt interdit est une contradiction directe.
    (Constaté le 2026-09-29 : une voiture dont le centre était hors champ
    débordait dans le cadre — un test sur le centre des objets la ratait.)
    """
    scene = bpy.context.scene
    cam = bpy.data.objects[nom_cam]
    kim = bpy.data.objects["KIM_racine"]
    bpy.context.view_layer.update()
    o = cam.matrix_world.translation
    if seuil_m is None:
        seuil_m = (Vector(kim.matrix_world.translation) - o).length - 3.0
    fr = [cam.matrix_world @ v for v in cam.data.view_frame(scene=scene)]
    dg = bpy.context.evaluated_depsgraph_get()
    sol = ("Chaussee", "Transversale", "Trottoir", "Passage")
    trouves = set()
    nx, ny = grille
    for i in range(nx):
        for j in range(ny):
            u, v = i / (nx - 1), j / (ny - 1)
            p = fr[2].lerp(fr[1], u).lerp(fr[3].lerp(fr[0], u), v)
            ok, loc, _, _, obj, _ = scene.ray_cast(dg, o, (p - o).normalized())
            if ok and (loc - o).length < seuil_m and not obj.name.startswith(sol):
                trouves.add(obj.name)
    return sorted(trouves)

# ATTENTION (2026-09-29) : world_to_camera_view renvoie une coordonnée x
# INVERSÉE pour un point situé derrière la caméra (profondeur z < 0). Toujours
# tester z avant d'interpréter x — sinon on écrit « droite » quand c'est l'inverse.
