"""Vue aérienne de la scène Blender pour le deck making-of (rendu sans toucher au .blend).

    /Applications/Blender.app/Contents/MacOS/Blender -b SCENE_BLENDER/avenue_greybox.blend \
        --python MAKING-OF/scripts/vue_aerienne_blender.py

Workbench, fond noir, décor gris, personnages (KIM, homme à terre, moto) en rouge, et les
caméras du film matérialisées par de petits cônes rouges. Le .blend n'est jamais sauvegardé.
"""
import bpy, math, os
from mathutils import Vector

OUT = os.path.join(os.path.dirname(bpy.data.filepath), "..", "MAKING-OF", "IMAGES", "09_blender_vue_aerienne.png")
sc = bpy.context.scene

# Emprise du décor (objets mesh visibles)
pts = [o.matrix_world @ Vector(c) for o in sc.objects if o.type == "MESH" and o.visible_get()
       for c in o.bound_box]
mn = Vector((min(p.x for p in pts), min(p.y for p in pts), 0))
mx = Vector((max(p.x for p in pts), max(p.y for p in pts), 0))
centre = (mn + mx) / 2
print("emprise", tuple(mn), tuple(mx))

# Héros en rouge : on colore par l'attribut objet (Workbench color = OBJECT)
ROUGE = (0.90, 0.20, 0.18, 1)
for o in sc.objects:
    o.color = (0.55, 0.55, 0.58, 1)
    if o.name.startswith(("KIM", "HOMME", "MOTO", "ADAM")):
        o.color = ROUGE

# Les caméras du film : un petit cône rouge à chaque position
for cam in [o for o in sc.objects if o.type == "CAMERA" and o.name.startswith("CAM_P")]:
    bpy.ops.mesh.primitive_cone_add(radius1=2.6, depth=4.5, location=cam.matrix_world.translation)
    c = bpy.context.active_object
    c.rotation_euler = cam.matrix_world.to_euler(); c.rotation_euler.x += math.pi
    c.color = ROUGE

# Caméra aérienne 3/4, centrée sur le carrefour où se joue l'action (autour de Kim)
cible = Vector((5.0, -12.0, 0.0))
cd = bpy.data.cameras.new("CAM_MAKINGOF_aerienne"); cd.lens = 32; cd.sensor_width = 36
cam = bpy.data.objects.new("CAM_MAKINGOF_aerienne", cd); sc.collection.objects.link(cam)
cam.location = cible + Vector((-95, -85, 230))
d = cible - cam.location
cam.rotation_euler = (math.pi / 2 + math.atan2(d.z, math.hypot(d.x, d.y)), 0, math.atan2(d.y, d.x) - math.pi / 2)
cd.clip_end = 2000
sc.camera = cam

# Rendu Workbench propre
sc.render.engine = "BLENDER_WORKBENCH"
sh = sc.display.shading
sh.light = "STUDIO"; sh.color_type = "OBJECT"
sh.show_cavity = True; sh.cavity_type = "BOTH"
sh.show_shadows = True; sh.shadow_intensity = 0.55
sh.show_object_outline = True; sh.object_outline_color = (0.05, 0.05, 0.06)
sc.display.shading.background_type = "VIEWPORT"
sc.display.shading.background_color = (0, 0, 0)
sc.render.film_transparent = False
w = bpy.context.scene.world
if w: w.color = (0, 0, 0)
sc.render.resolution_x, sc.render.resolution_y, sc.render.resolution_percentage = 2560, 1440, 100
sc.render.image_settings.file_format = "PNG"
sc.render.filepath = os.path.abspath(OUT)
sc.frame_set(1)
bpy.ops.render.render(write_still=True)
print("RENDU", os.path.abspath(OUT))
