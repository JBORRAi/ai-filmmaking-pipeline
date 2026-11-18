"""Foule de piétons en blocs, sur les trottoirs.

Sert surtout aux plans au téléobjectif : au 200 mm, la foule se compresse en
strates et c'est elle qui fait la densité new-yorkaise. Sans foule, pas d'écrasement.

    exec(open('.../scripts/foule.py').read())
    peupler(x_min=-90, x_max=20, densite=0.55)
"""
import bpy
import random

BORD_TROTTOIR = 15.0
TROTTOIR = 6.0
H_TROTTOIR = 0.15


def _collection(nom):
    if nom in bpy.data.collections:
        return bpy.data.collections[nom]
    col = bpy.data.collections.new(nom)
    bpy.context.scene.collection.children.link(col)
    return col


def peupler(x_min=-90.0, x_max=20.0, densite=0.5, graine=7):
    """densite = piétons par mètre linéaire et par trottoir."""
    random.seed(graine)
    col = _collection("FOULE")
    for ob in list(col.objects):
        bpy.data.objects.remove(ob, do_unlink=True)

    mat = bpy.data.materials.get("gris_pieton") or bpy.data.materials.new("gris_pieton")
    mat.use_nodes = True
    bsdf = next((n for n in mat.node_tree.nodes if n.type == "BSDF_PRINCIPLED"), None)
    if bsdf:
        bsdf.inputs["Base Color"].default_value = (0.34, 0.33, 0.32, 1)
        bsdf.inputs["Roughness"].default_value = 0.9

    n = 0
    for signe in (-1, 1):
        x = x_min
        while x < x_max:
            x += random.expovariate(densite)
            if x > x_max:
                break
            # Position en travers du trottoir, sans coller aux façades
            offset = random.uniform(0.9, TROTTOIR - 0.9)
            y = signe * (BORD_TROTTOIR + offset)
            hauteur = random.uniform(1.60, 1.92)
            largeur = random.uniform(0.42, 0.58)
            bpy.ops.mesh.primitive_cube_add(
                size=1.0, location=(x, y, H_TROTTOIR + hauteur / 2))
            ob = bpy.context.active_object
            ob.name = f"Pieton_{n:03d}"
            ob.scale = (largeur * 0.62, largeur, hauteur)
            ob.rotation_euler = (0, 0, random.uniform(-0.4, 0.4))
            # transform_apply : les trois paramètres sont passés explicitement.
            # L'opérateur mémorise ses derniers réglages ; une translation appliquée
            # par erreur remet ob.location à zéro et fausse tout calcul de distance.
            bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
            ob.data.materials.append(mat)
            for c in ob.users_collection:
                c.objects.unlink(ob)
            col.objects.link(ob)
            n += 1
    return n


def degager(x_centre, rayon=1.6):
    """Retire les piétons trop proches d'un point (pour dégager Kim)."""
    col = bpy.data.collections.get("FOULE")
    if not col:
        return 0
    retires = 0
    for ob in list(col.objects):
        dx = ob.location.x - x_centre[0]
        dy = ob.location.y - x_centre[1]
        if (dx * dx + dy * dy) ** 0.5 < rayon:
            bpy.data.objects.remove(ob, do_unlink=True)
            retires += 1
    return retires
