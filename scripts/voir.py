"""Bascule la vue 3D de Blender sur la caméra d'un plan, cadre exact et rendu.

    exec(open('./KIMKATCHER/EP01/scripts/voir.py').read())
    voir("P02")          # ou "CAM_P02_tele_200"
    plans()              # liste les plans disponibles
"""
import bpy


def _zone_vue3d():
    for fenetre in bpy.context.window_manager.windows:
        for area in fenetre.screen.areas:
            if area.type == "VIEW_3D":
                region = next((r for r in area.regions if r.type == "WINDOW"), None)
                if region:
                    return fenetre, area, region
    return None, None, None


def plans():
    col = bpy.data.collections.get("CAMERAS")
    noms = sorted(o.name for o in col.objects) if col else []
    for n in noms:
        print(f"  {n}  ({bpy.data.objects[n].data.lens:.0f} mm)")
    return noms


def voir(plan, rendu=True, ecran_propre=True):
    """`plan` : "P02", "CAM_P02_tele_200", ou un nom complet."""
    col = bpy.data.collections.get("CAMERAS")
    if col is None:
        raise RuntimeError("Pas de collection CAMERAS — lancer rig_camera.py d'abord.")

    cam = bpy.data.objects.get(plan)
    if cam is None:
        cles = [o for o in col.objects if f"_{plan}_" in o.name or o.name.startswith(f"CAM_{plan}")]
        if not cles:
            raise ValueError(f"Plan introuvable : {plan}. Disponibles : "
                             + ", ".join(sorted(o.name for o in col.objects)))
        cam = cles[0]

    scene = bpy.context.scene
    scene.camera = cam

    # Le passepartout noircit tout ce qui déborde du cadre : on ne juge
    # que ce qui sera réellement à l'image.
    cam.data.show_passepartout = True
    cam.data.passepartout_alpha = 1.0

    fenetre, area, region = _zone_vue3d()
    if area is None:
        raise RuntimeError("Aucune vue 3D ouverte dans Blender.")

    espace = area.spaces[0]
    espace.region_3d.view_perspective = "CAMERA"
    espace.shading.type = "RENDERED" if rendu else "SOLID"
    if ecran_propre:
        espace.overlay.show_overlays = False
        espace.show_gizmo = False
    espace.lock_camera = False

    # Ajuster le cadre caméra à la zone de vue
    with bpy.context.temp_override(window=fenetre, area=area, region=region):
        bpy.ops.view3d.view_center_camera()

    print(f"Vue → {cam.name} ({cam.data.lens:.0f} mm)  "
          f"ratio {scene.render.resolution_x}x{scene.render.resolution_y}")
    return cam.name
