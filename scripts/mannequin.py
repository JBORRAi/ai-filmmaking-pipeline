"""Mannequin humain grossier — sert de guide de structure pour l'habillage.

Un bloc abstrait ne dit rien à un modèle d'image : il faut une silhouette
reconnaissable (tête, torse, bras, jambes) pour que la pose et l'échelle soient
comprises. Proportions réelles, 1,78 m.

    exec(open('.../scripts/mannequin.py').read())
    mannequin("KIM", (-45.0, -17.6), orientation=180)  # 180° = face à la caméra
"""
import bpy
import math

TAILLE = 1.78


def _collection(nom):
    if nom in bpy.data.collections:
        return bpy.data.collections[nom]
    col = bpy.data.collections.new(nom)
    bpy.context.scene.collection.children.link(col)
    return col


def _piece(nom, col, mat, centre, dims, parent=None):
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=centre)
    ob = bpy.context.active_object
    ob.name = nom
    ob.scale = dims
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    for c in ob.users_collection:
        c.objects.unlink(ob)
    col.objects.link(ob)
    if parent:
        ob.parent = parent
    return ob


def mannequin(nom, position_xy, orientation=180.0, sol=0.15, couleur=(0.20, 0.20, 0.22, 1)):
    """`orientation` en degrés : 180 = tourné vers -X (donc face à une caméra en -X)."""
    col = _collection("MANNEQUINS")
    for ob in list(col.objects):
        if ob.name.startswith(f"{nom}_"):
            bpy.data.objects.remove(ob, do_unlink=True)

    mat = bpy.data.materials.get("mat_mannequin") or bpy.data.materials.new("mat_mannequin")
    mat.use_nodes = True
    bsdf = next((n for n in mat.node_tree.nodes if n.type == "BSDF_PRINCIPLED"), None)
    if bsdf:
        bsdf.inputs["Base Color"].default_value = couleur
        bsdf.inputs["Roughness"].default_value = 0.75

    x, y = position_xy
    # Racine : un vide, pour pouvoir tourner et déplacer l'ensemble
    bpy.ops.object.empty_add(type="PLAIN_AXES", location=(x, y, sol))
    racine = bpy.context.active_object
    racine.name = f"{nom}_racine"
    racine.empty_display_size = 0.3
    for c in racine.users_collection:
        c.objects.unlink(racine)
    col.objects.link(racine)

    # Proportions humaines (fractions de la taille), en coordonnées locales
    pieces = [
        # nom,        centre (x, y, z),        dimensions (prof, larg, haut)
        ("tete",      (0.00, 0.00, 1.66),      (0.19, 0.16, 0.24)),
        ("cou",       (0.00, 0.00, 1.50),      (0.11, 0.11, 0.09)),
        ("torse",     (0.00, 0.00, 1.20),      (0.24, 0.42, 0.52)),
        ("bassin",    (0.00, 0.00, 0.90),      (0.22, 0.34, 0.20)),
        ("bras_g",    (0.00, 0.26, 1.20),      (0.13, 0.13, 0.52)),
        ("bras_d",    (0.00, -0.26, 1.20),     (0.13, 0.13, 0.52)),
        ("jambe_g",   (0.00, 0.11, 0.42),      (0.16, 0.17, 0.84)),
        ("jambe_d",   (0.00, -0.11, 0.42),     (0.16, 0.17, 0.84)),
    ]
    for pn, centre, dims in pieces:
        ob = _piece(f"{nom}_{pn}", col, mat,
                    (x + centre[0], y + centre[1], sol + centre[2]), dims, parent=racine)
        ob.data.materials.append(mat)
        ob.matrix_parent_inverse = racine.matrix_world.inverted()

    racine.rotation_euler = (0, 0, math.radians(orientation))
    bpy.context.view_layer.update()
    return racine
