import bpy
import os
import sys
import math
import functools

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import utils


# Arguments
filename = "./dots.png"
resolution_percentage = 20
num_samples = 50


# Map
objects = bpy.data.objects
scene = bpy.context.scene
camera = bpy.data.objects["Camera"]
light = bpy.data.objects["Light"]

select_all = functools.partial(bpy.ops.object.select_all, action="SELECT")
deselect_all = functools.partial(bpy.ops.object.select_all, action="DESELECT")
add_cube = bpy.ops.mesh.primitive_cube_add
resize = bpy.ops.transform.resize
delete = bpy.ops.object.delete


# Clear scene
select_all()
light.select_set(False)
camera.select_set(False)
delete()


# Draw
rotation_x = math.radians(45)

add_cube(location=(0, 0, 2), rotation=(rotation_x, 0, 0))
c1 = bpy.context.object

add_cube(location=(0, 0, 0), rotation=(rotation_x, 0, 0))
c2 = bpy.context.object

add_cube(location=(0, -2, 0), rotation=(rotation_x, 0, 0))
c3 = bpy.context.object

add_cube(location=(0, 2, 0), rotation=(rotation_x, 0, 0))
c4 = bpy.context.object


# Modify
deselect_all()
c1.select_set(True)
resize(value=(1, 0.5, 0.5))


# Export
utils.set_output_properties(scene, resolution_percentage, filename)
utils.set_cycles_renderer(scene, camera, num_samples)
bpy.ops.wm.save_as_mainfile(filepath="./dots.blend")
