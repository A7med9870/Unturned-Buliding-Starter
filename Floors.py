import bpy
import bmesh
import os
import webbrowser
from mathutils import Vector
from bpy.props import (StringProperty, PointerProperty, EnumProperty, BoolProperty)
from bpy.types import (Panel, Operator, AddonPreferences, PropertyGroup, Menu)
from bpy.utils import previews

class OBJECT_OT_add_Floor_from_blend(Operator):
    """Floor 5X5"""
    bl_idname = "mesh.add_normal_floor_from_blend"
    bl_label = "Floor"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        preferences = bpy.context.preferences.addons['NewObjectTestKalb'].preferences
        return preferences.show_Floors_objects_panel

    def execute(self, context):
        addon_dir = os.path.dirname(__file__)
        blend_filename = "U3D.blend"
        object_name = "Floor"
        load_object_from_blend(addon_dir, blend_filename, object_name)
        return {'FINISHED'}

class OBJECT_MT_add_object_menu_floors(Menu):
    bl_label = "U3 Floors"
    bl_idname = "OBJECT_MT_add_object_menu_floors"

    @classmethod
    def poll(cls, context):
        preferences = bpy.context.preferences.addons['NewObjectTestKalb'].preferences
        return preferences.show_Floors_objects_panel

    def draw(self, context):
        layout = self.layout
        layout.operator(OBJECT_OT_add_Floor_from_blend.bl_idname, icon_value=custom_icons["custom_icon"].icon_id)

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
            cursor_location = bpy.context.scene.cursor.location
            obj.location = cursor_location
            break

def add_object_menu(self, context):
    layout = self.layout
    layout.menu("OBJECT_MT_add_object_menu_floors", icon_value=custom_icons["custom_icon"].icon_id)

classes = (
    OBJECT_OT_add_Floor_from_blend,
    OBJECT_MT_add_object_menu_floors
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    global custom_icons
    custom_icons = previews.new()
    icon_file = os.path.join(os.path.dirname(__file__), "icons", "Floor.png")
    custom_icons.load("custom_icon", icon_file, 'IMAGE')

    bpy.types.VIEW3D_MT_mesh_add.append(add_object_menu)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    global custom_icons
    previews.remove(custom_icons)
    bpy.types.VIEW3D_MT_mesh_add.remove(add_object_menu)

if __name__ == "__main__":
    register()