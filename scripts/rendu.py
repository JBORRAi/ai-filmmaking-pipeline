"""Rend un plan depuis sa caméra, en 2.39:1, vers renders/.

    exec(open('.../scripts/rendu.py').read())
    rendre("CAM_P01_large_24")           # -> renders/CAM_P01_large_24.png
"""
import bpy
import os

DOSSIER = "./KIMKATCHER/EP01/_travail/rendus"   # brouillons
PLANS = "./KIMKATCHER/EP01/PLANS"


def dossier_plan(plan, sous="1_BLENDER"):
    """PLANS/<plan>_*/<sous>/ — ex. dossier_plan("P06") -> .../PLANS/P06_cri/1_BLENDER"""
    import glob
    cands = [c for c in glob.glob(os.path.join(PLANS, f"{plan}_*"))
             if os.path.basename(c).split("_")[0] == plan]
    if not cands:
        raise ValueError(f"Aucun dossier de plan pour {plan} dans {PLANS}")
    d = os.path.join(cands[0], sous)
    os.makedirs(d, exist_ok=True)
    return d


def rendre(nom_cam, suffixe="", samples=16, large=1600):
    os.makedirs(DOSSIER, exist_ok=True)
    scene = bpy.context.scene
    cam = bpy.data.objects.get(nom_cam)
    if cam is None:
        raise ValueError(f"Caméra introuvable : {nom_cam}")
    scene.camera = cam

    scene.render.resolution_x = large
    scene.render.resolution_y = int(large / 2.39)
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "PNG"
    if hasattr(scene, "eevee"):
        try:
            scene.eevee.taa_render_samples = samples
        except AttributeError:
            pass

    chemin = os.path.join(DOSSIER, f"{nom_cam}{suffixe}.png")
    scene.render.filepath = chemin
    bpy.ops.render.render(write_still=True)
    return chemin
