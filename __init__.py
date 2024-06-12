bl_info = {
    "name": "Unturned Buildings Starter",
    "author": "A7med9870",
    "version": (1, 0),
    "blender": (4, 1, 0),
    "location": "View3D > Add > Mesh > Add Object from Blend File",
    "description": "Adds your desired unturned building model to the scene",
    "warning": "",
    "doc_url": "",
    "category": "Add Mesh",
}

import bpy
import os
from bpy.types import Operator, Menu

def load_object_from_blend(addon_dir, blend_filename, object_name):
    filepath = os.path.join(addon_dir, blend_filename)
    with bpy.data.libraries.load(filepath, link=False) as (data_from, data_to):
        if object_name in data_from.objects:
            data_to.objects.append(object_name)
    
    for obj in data_to.objects:
        if obj.name == object_name:
            obj.name = object_name + "_imported"  # Make the name unique
            bpy.context.collection.objects.link(obj)
            bpy.context.view_layer.objects.active = obj
            obj.select_set(True)
            
            # Move the object towards the 3D cursor
            cursor_location = bpy.context.scene.cursor.location
            obj.location = cursor_location
            
            break

class OBJECT_OT_add_garage_door_from_blend(Operator):
    """Garage Door 5X5"""
    bl_idname = "mesh.add_garage_door_from_blend"
    bl_label = "Garage Door"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        addon_dir = os.path.dirname(__file__)
        blend_filename = "U3D.blend"  # Replace with your blend file name
        object_name = "Garage Door"  # Replace with the name of your object
        load_object_from_blend(addon_dir, blend_filename, object_name)
        return {'FINISHED'}

class OBJECT_OT_add_door_from_blend(Operator):
    """Door 5X5"""
    bl_idname = "mesh.add_door_from_blend"
    bl_label = "Door"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        addon_dir = os.path.dirname(__file__)
        blend_filename = "U3D.blend"
        object_name = "Door"
        load_object_from_blend(addon_dir, blend_filename, object_name)
        return {'FINISHED'}
        
        
class OBJECT_OT_add_Elevator_Door_from_blend(Operator):
    """Elevator door 5X5"""
    bl_idname = "mesh.add_elevator_door_from_blend"
    bl_label = "Elevator door"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        addon_dir = os.path.dirname(__file__)
        blend_filename = "U3D.blend"
        object_name = "Elevator Door"
        load_object_from_blend(addon_dir, blend_filename, object_name)
        return {'FINISHED'}

class OBJECT_OT_add_normal_Window_from_blend(Operator):
    """Normal Window 5X5"""
    bl_idname = "mesh.add_normal_window_from_blend"
    bl_label = "A Window"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        addon_dir = os.path.dirname(__file__)
        blend_filename = "U3D.blend"
        object_name = "Window"
        load_object_from_blend(addon_dir, blend_filename, object_name)
        return {'FINISHED'}
        
class OBJECT_OT_add_Mall_Window_from_blend(Operator):
    """Mall Window 5X5"""
    bl_idname = "mesh.add_mall_window_from_blend"
    bl_label = "Mall Window"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        addon_dir = os.path.dirname(__file__)
        blend_filename = "U3D.blend"
        object_name = "Mall Window"
        load_object_from_blend(addon_dir, blend_filename, object_name)
        return {'FINISHED'}

class OBJECT_OT_add_door_frame_from_blend(Operator):
    """Frame Of DoorWay"""
    bl_idname = "mesh.add_door_frame_from_blend"
    bl_label = "Door Frame"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        addon_dir = os.path.dirname(__file__)
        blend_filename = "U3D.blend"
        object_name = "Door Frame"
        load_object_from_blend(addon_dir, blend_filename, object_name)
        return {'FINISHED'}

class OBJECT_OT_add_door_garage_frame_from_blend(Operator):
    """Frame Of garage door"""
    bl_idname = "mesh.add_door_garage_frame_from_blend"
    bl_label = "Garage Door Frame"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        addon_dir = os.path.dirname(__file__)
        blend_filename = "U3D.blend"
        object_name = "Garage Door Frame"
        load_object_from_blend(addon_dir, blend_filename, object_name)
        return {'FINISHED'}

class OBJECT_OT_add_window_frame_from_blend(Operator):
    """Frame Of window"""
    bl_idname = "mesh.add_window_a_frame_from_blend"
    bl_label = "Window Frame"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        addon_dir = os.path.dirname(__file__)
        blend_filename = "U3D.blend"
        object_name = "Window Frame"
        load_object_from_blend(addon_dir, blend_filename, object_name)
        return {'FINISHED'}


class OBJECT_OT_add_Wall_from_blend(Operator):
    """Wall 5X5"""
    bl_idname = "mesh.add_normal_wall_from_blend"  # Corrected bl_idname
    bl_label = "A Normal wall"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        addon_dir = os.path.dirname(__file__)
        blend_filename = "U3D.blend"
        object_name = "Wall"
        load_object_from_blend(addon_dir, blend_filename, object_name)
        return {'FINISHED'}
 
class OBJECT_OT_add_Floor_from_blend(Operator):
    """Floor 5X5"""
    bl_idname = "mesh.add_normal_flooor_from_blend"
    bl_label = "Floor"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        addon_dir = os.path.dirname(__file__)
        blend_filename = "U3D.blend"
        object_name = "Floor"
        load_object_from_blend(addon_dir, blend_filename, object_name)
        return {'FINISHED'}
        
#Roofup
class OBJECT_OT_add_Roofup_from_blend(Operator):
    """Roof 5X5"""
    bl_idname = "mesh.add_normal_roofup_from_blend"
    bl_label = "Roof"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        addon_dir = os.path.dirname(__file__)
        blend_filename = "U3D.blend"
        object_name = "Roofup"
        load_object_from_blend(addon_dir, blend_filename, object_name)
        return {'FINISHED'}

class OBJECT_OT_add_cWall_from_blend(Operator):
    """Corner wall 5X5"""
    bl_idname = "mesh.add_normal_cwall_from_blend"
    bl_label = "Corner wall"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        addon_dir = os.path.dirname(__file__)
        blend_filename = "U3D.blend"
        object_name = "Corner Wall"
        load_object_from_blend(addon_dir, blend_filename, object_name)
        return {'FINISHED'}

class OBJECT_OT_add_Wall_zf_corner_from_blend(Operator):
    """Wall zf corner 5X5"""
    bl_idname = "mesh.add_normal_wall_zf_corner_from_blend"
    bl_label = "Wall zf corner"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        addon_dir = os.path.dirname(__file__)
        blend_filename = "U3D.blend"
        object_name = "Wall_zf_corner"
        load_object_from_blend(addon_dir, blend_filename, object_name)
        return {'FINISHED'}
        
class OBJECT_OT_add_Corner_from_blend(Operator):
    """Corner Stairs 180 degree"""
    bl_idname = "mesh.add_corner_stairs_from_blend"
    bl_label = "Corner Stairs"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        addon_dir = os.path.dirname(__file__)
        blend_filename = "U3D.blend"
        object_name = "Corner Stairs"
        load_object_from_blend(addon_dir, blend_filename, object_name)
        return {'FINISHED'}
        
class OBJECT_OT_add_Stairs_from_blend(Operator):
    """Stairs 5X5"""
    bl_idname = "mesh.add_stairs_from_blend"
    bl_label = "Stairs"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        addon_dir = os.path.dirname(__file__)
        blend_filename = "U3D.blend"
        object_name = "Stairs"
        load_object_from_blend(addon_dir, blend_filename, object_name)
        return {'FINISHED'}
        
class OBJECT_OT_add_Ramp_from_blend(Operator):
    """Ramp 5X5"""
    bl_idname = "mesh.add_normal_ramp_from_blend"
    bl_label = "Ramp"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        addon_dir = os.path.dirname(__file__)
        blend_filename = "U3D.blend"
        object_name = "Ramp"
        load_object_from_blend(addon_dir, blend_filename, object_name)
        return {'FINISHED'}
#LongStairs       
class OBJECT_OT_add_LongStairs_from_blend(Operator):
    """Long Stairs 5X10"""
    bl_idname = "mesh.add_long_stairs_from_blend"
    bl_label = "Long Stairs"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        addon_dir = os.path.dirname(__file__)
        blend_filename = "U3D.blend"
        object_name = "LongStairs"
        load_object_from_blend(addon_dir, blend_filename, object_name)
        return {'FINISHED'}

class OBJECT_OT_add_LongRamp_from_blend(Operator):
    """Long Ramp 5X10"""
    bl_idname = "mesh.add_long_ramp_from_blend"
    bl_label = "Long Ramp"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        addon_dir = os.path.dirname(__file__)
        blend_filename = "U3D.blend"
        object_name = "LongRamp"
        load_object_from_blend(addon_dir, blend_filename, object_name)
        return {'FINISHED'}
#Character
class OBJECT_OT_add_Character_from_blend(Operator):
    """Player Character Reference"""
    bl_idname = "mesh.add_character_from_blend"
    bl_label = "Character"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        addon_dir = os.path.dirname(__file__)
        blend_filename = "U3D.blend"
        object_name = "Character"
        load_object_from_blend(addon_dir, blend_filename, object_name)
        return {'FINISHED'}

class OBJECT_OT_add_rampart_railing_from_blend(Operator):
    """A fancy rampart with railing"""
    bl_idname = "mesh.add_rampart_railing_from_blend"
    bl_label = "Rampart with railing"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        addon_dir = os.path.dirname(__file__)
        blend_filename = "U3D.blend"
        object_name = "Rampart railing"
        load_object_from_blend(addon_dir, blend_filename, object_name)
        return {'FINISHED'}

#Rampart

class OBJECT_OT_add_rampart_from_blend(Operator):
    """Rampart, just a Rampart"""
    bl_idname = "mesh.add_rampart_from_blend"
    bl_label = "Rampart"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        addon_dir = os.path.dirname(__file__)
        blend_filename = "U3D.blend"
        object_name = "Rampart"
        load_object_from_blend(addon_dir, blend_filename, object_name)
        return {'FINISHED'}


#THE FING Menus, They are neccasry for sparting this menu into their own shit parts____________________________________________________________________________________________________________
class OBJECT_MT_add_object_menu_doors(Menu):
    bl_label = "U3 Doors"
    bl_idname = "OBJECT_MT_add_object_menu_doors"

    def draw(self, context):
        layout = self.layout
        layout.operator(OBJECT_OT_add_garage_door_from_blend.bl_idname)
        layout.operator(OBJECT_OT_add_door_from_blend.bl_idname)
        layout.operator(OBJECT_OT_add_Elevator_Door_from_blend.bl_idname)
        layout.operator(OBJECT_OT_add_door_frame_from_blend.bl_idname)
        layout.operator(OBJECT_OT_add_door_garage_frame_from_blend.bl_idname)

class OBJECT_MT_add_object_menu_windows(Menu):
    bl_label = "U3 Windows"
    bl_idname = "OBJECT_MT_ao_menu_windows"

    def draw(self, context):
        layout = self.layout
        layout.operator(OBJECT_OT_add_normal_Window_from_blend.bl_idname)
        layout.operator(OBJECT_OT_add_Mall_Window_from_blend.bl_idname)
        layout.operator(OBJECT_OT_add_window_frame_from_blend.bl_idname)
        
class OBJECT_MT_add_object_menu_ramparts(Menu):
    bl_label = "U3 ramparts"
    bl_idname = "OBJECT_MT_ao_menu_ramparts"

    def draw(self, context):
        layout = self.layout
        layout.operator(OBJECT_OT_add_rampart_railing_from_blend.bl_idname)
        layout.operator(OBJECT_OT_add_rampart_from_blend.bl_idname)
        

class OBJECT_MT_refernces_menu_Stairs(Menu):
    bl_label = "U3 Refernces"
    bl_idname = "OBJECT_MT_ao_menu_refernces"

    def draw(self, context):
        layout = self.layout
        layout.operator(OBJECT_OT_add_Character_from_blend.bl_idname)

class OBJECT_MT_add_object_menu_Stairs(Menu):
    bl_label = "U3 Stairs"
    bl_idname = "OBJECT_MT_ao_menu_stairs"

    def draw(self, context):
        layout = self.layout
        layout.operator(OBJECT_OT_add_Stairs_from_blend.bl_idname)
        layout.operator(OBJECT_OT_add_Corner_from_blend.bl_idname)
        layout.operator(OBJECT_OT_add_LongStairs_from_blend.bl_idname)

class OBJECT_MT_add_object_menu_windows(Menu):
    bl_label = "U3 Windows"
    bl_idname = "OBJECT_MT_ao_menu_windows"

    def draw(self, context):
        layout = self.layout
        layout.operator(OBJECT_OT_add_normal_Window_from_blend.bl_idname)
        layout.operator(OBJECT_OT_add_Mall_Window_from_blend.bl_idname)
        
class OBJECT_MT_add_object_menu_Floors(Menu):
    bl_label = "U3 Floors"
    bl_idname = "OBJECT_MT_ao_menu_Floors"

    def draw(self, context):
        layout = self.layout
        layout.operator(OBJECT_OT_add_Roofup_from_blend.bl_idname)
        layout.operator(OBJECT_OT_add_Floor_from_blend.bl_idname)

#THE ADDER TO UI, YOU NEED TO ACTULLY FING SEE THIS SHIT IN THE ADD MESH MENU___________________________________________________________________________________
class OBJECT_MT_add_object_menu_Walls(Menu):
    bl_label = "U3 Walls"
    bl_idname = "OBJECT_MT_ao_menu_walls"

    def draw(self, context):
        layout = self.layout
        layout.operator(OBJECT_OT_add_Wall_from_blend.bl_idname)
        layout.operator(OBJECT_OT_add_Wall_zf_corner_from_blend.bl_idname)
        layout.operator(OBJECT_OT_add_cWall_from_blend.bl_idname)
        layout.operator(OBJECT_OT_add_window_frame_from_blend.bl_idname)

#LOADS THE FING MENUS____________________________________________________________________________________________________________________________________________
def add_object_menu(self, context):
    self.layout.menu(OBJECT_MT_add_object_menu_Floors.bl_idname)
    self.layout.menu(OBJECT_MT_add_object_menu_doors.bl_idname)
    self.layout.menu(OBJECT_MT_add_object_menu_windows.bl_idname)
    self.layout.menu(OBJECT_MT_add_object_menu_Walls.bl_idname)
    self.layout.menu(OBJECT_MT_add_object_menu_Stairs.bl_idname)
    self.layout.menu(OBJECT_MT_add_object_menu_ramparts.bl_idname)
    self.layout.menu(OBJECT_MT_refernces_menu_Stairs.bl_idname)


def register():
    bpy.utils.register_class(OBJECT_OT_add_garage_door_from_blend)
    bpy.utils.register_class(OBJECT_OT_add_door_from_blend)
    bpy.utils.register_class(OBJECT_MT_refernces_menu_Stairs)
    bpy.utils.register_class(OBJECT_MT_add_object_menu_doors)
    bpy.utils.register_class(OBJECT_OT_add_normal_Window_from_blend)
    bpy.utils.register_class(OBJECT_OT_add_Floor_from_blend)
    bpy.utils.register_class(OBJECT_OT_add_Roofup_from_blend)
    bpy.utils.register_class(OBJECT_OT_add_Mall_Window_from_blend)
    bpy.utils.register_class(OBJECT_OT_add_window_frame_from_blend)
    bpy.utils.register_class(OBJECT_OT_add_Wall_from_blend)
    bpy.utils.register_class(OBJECT_OT_add_Wall_zf_corner_from_blend)
    bpy.utils.register_class(OBJECT_MT_add_object_menu_windows)
    bpy.utils.register_class(OBJECT_MT_add_object_menu_Floors)
    bpy.utils.register_class(OBJECT_MT_add_object_menu_Walls)
    bpy.utils.register_class(OBJECT_OT_add_cWall_from_blend)
    bpy.utils.register_class(OBJECT_OT_add_Elevator_Door_from_blend)
    bpy.utils.register_class(OBJECT_OT_add_door_frame_from_blend)
    bpy.utils.register_class(OBJECT_OT_add_door_garage_frame_from_blend)
    bpy.utils.register_class(OBJECT_MT_add_object_menu_ramparts)
    bpy.utils.register_class(OBJECT_MT_add_object_menu_Stairs)
    bpy.utils.register_class(OBJECT_OT_add_Corner_from_blend)
    bpy.utils.register_class(OBJECT_OT_add_Ramp_from_blend)
    bpy.utils.register_class(OBJECT_OT_add_LongStairs_from_blend)
    bpy.utils.register_class(OBJECT_OT_add_LongRamp_from_blend)
    bpy.utils.register_class(OBJECT_OT_add_Character_from_blend)
    bpy.utils.register_class(OBJECT_OT_add_rampart_railing_from_blend)
    bpy.utils.register_class(OBJECT_OT_add_rampart_from_blend)
    bpy.utils.register_class(OBJECT_OT_add_Stairs_from_blend)
    bpy.types.VIEW3D_MT_mesh_add.append(add_object_menu)
    

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_add_garage_door_from_blend)
    bpy.utils.unregister_class(OBJECT_OT_add_door_from_blend)
    bpy.utils.unregister_class(OBJECT_MT_refernces_menu_Stairs)
    bpy.utils.unregister_class(OBJECT_OT_add_Corner_from_blend)
    bpy.utils.unregister_class(OBJECT_MT_add_object_menu_doors)
    bpy.utils.unregister_class(OBJECT_MT_add_object_menu_windows)
    bpy.utils.unregister_class(OBJECT_OT_add_Floor_from_blend)
    bpy.utils.unregister_class(OBJECT_MT_add_object_menu_Floors)
    bpy.utils.unregister_class(OBJECT_OT_add_normal_Window_from_blend)
    bpy.utils.unregister_class(OBJECT_OT_add_Mall_Window_from_blend)
    bpy.utils.unregister_class(OBJECT_OT_add_window_frame_from_blend)
    bpy.utils.unregister_class(OBJECT_OT_add_Wall_from_blend)
    bpy.utils.unregister_class(OBJECT_OT_add_Wall_zf_corner_from_blend)
    bpy.utils.unregister_class(OBJECT_OT_add_Roofup_from_blend)
    bpy.utils.unregister_class(OBJECT_MT_add_object_menu_Walls)
    bpy.utils.unregister_class(OBJECT_OT_add_cWall_from_blend)
    bpy.utils.unregister_class(OBJECT_MT_add_object_menu_Stairs)
    bpy.utils.unregister_class(OBJECT_OT_add_Elevator_Door_from_blend)
    bpy.utils.unregister_class(OBJECT_OT_add_door_frame_from_blend)
    bpy.utils.unregister_class(OBJECT_OT_add_door_garage_frame_from_blend)
    bpy.utils.unregister_class(OBJECT_MT_add_object_menu_ramparts)
    bpy.utils.unregister_class(OBJECT_OT_add_Stairs_from_blend)
    bpy.utils.unregister_class(OBJECT_OT_add_Ramp_from_blend)
    bpy.utils.unregister_class(OBJECT_OT_add_LongRamp_from_blend)
    bpy.utils.unregister_class(OBJECT_OT_add_LongStairs_from_blend)
    bpy.utils.unregister_class(OBJECT_OT_add_Character_from_blend)
    bpy.utils.unregister_class(OBJECT_OT_add_rampart_railing_from_blend)
    bpy.utils.unregister_class(OBJECT_OT_add_rampart_from_blend)
    bpy.types.VIEW3D_MT_mesh_add.remove(add_object_menu)

if __name__ == "__main__":
    register()
