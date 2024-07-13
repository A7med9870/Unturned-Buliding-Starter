import bpy
import bmesh
import os
import webbrowser
from mathutils import Vector
from bpy.props import (StringProperty, PointerProperty, EnumProperty, BoolProperty)
from bpy.types import (Panel, Operator, AddonPreferences, PropertyGroup, Menu)
from bpy.utils import previews

class OBJECT_OT_add_normal_Window_from_blend(Operator):
    """Normal Window 5X5"""
    bl_idname = "mesh.add_normal_window_from_blend"
    bl_label = "A Window"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        preferences = bpy.context.preferences.addons['NewObjectTestKalb'].preferences
        return preferences.show_windows_objects_panel

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

class OBJECT_OT_add_Eastern_Window_from_blend(Operator):
    """Mall Window 5X5"""
    bl_idname = "mesh.add_eastern_window_from_blend"
    bl_label = "Eastern Window"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        addon_dir = os.path.dirname(__file__)
        blend_filename = "U3D.blend"
        object_name = "Eastern_Window"
        load_object_from_blend(addon_dir, blend_filename, object_name)
        return {'FINISHED'}

class OBJECT_OT_add_Eastern_Window_Frame_from_blend(Operator):
    """Mall Window 5X5"""
    bl_idname = "mesh.add_eastern_window_frame_from_blend"
    bl_label = "Eastern Window Frame"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        addon_dir = os.path.dirname(__file__)
        blend_filename = "U3D.blend"
        object_name = "Eastern_Window_frame"
        load_object_from_blend(addon_dir, blend_filename, object_name)
        return {'FINISHED'}
#Window vent
class OBJECT_OT_add_Window_Vent_from_blend(Operator):
    """Mall Window 5X5"""
    bl_idname = "mesh.add_window_vent_from_blend"
    bl_label = "Window vent"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        addon_dir = os.path.dirname(__file__)
        blend_filename = "U3D.blend"
        object_name = "Window vent"
        load_object_from_blend(addon_dir, blend_filename, object_name)
        return {'FINISHED'}
#Circle_window
class OBJECT_OT_add_Window_Circle_t_from_blend(Operator):
    """Mall Window 5X5"""
    bl_idname = "mesh.add_window_circlue_from_blend"
    bl_label = "Circle_window"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        addon_dir = os.path.dirname(__file__)
        blend_filename = "U3D.blend"
        object_name = "Circle_window"
        load_object_from_blend(addon_dir, blend_filename, object_name)
        return {'FINISHED'}
#Circle_window_frame
class OBJECT_OT_add_Window_Circle_frame_from_blend(Operator):
    """Mall Window 5X5"""
    bl_idname = "mesh.add_window_circlue_frame_blend"
    bl_label = "Circle_window_frame"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        addon_dir = os.path.dirname(__file__)
        blend_filename = "U3D.blend"
        object_name = "Circle_window_frame"
        load_object_from_blend(addon_dir, blend_filename, object_name)
        return {'FINISHED'}
class OBJECT_OT_add_Window_Vent_Frame_from_blend(Operator):
    """Mall Window 5X5"""
    bl_idname = "mesh.add_window_vent_frame_from_blend"
    bl_label = "Window Vent Frame"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        addon_dir = os.path.dirname(__file__)
        blend_filename = "U3D.blend"
        object_name = "Window vent frame"
        load_object_from_blend(addon_dir, blend_filename, object_name)
        return {'FINISHED'}

class OBJECT_OT_add_Small_Window_from_blend(Operator):
    """Mall Window 5X5"""
    bl_idname = "mesh.add_window_small_from_blend"
    bl_label = "Small_Window"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        addon_dir = os.path.dirname(__file__)
        blend_filename = "U3D.blend"
        object_name = "Small_Window"
        load_object_from_blend(addon_dir, blend_filename, object_name)
        return {'FINISHED'}

class OBJECT_OT_add_wide_Window_frame_from_blend(Operator):
    """Mall Window 5X5"""
    bl_idname = "mesh.add_window_wide_frame_from_blend"
    bl_label = "Wide Window Frame"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        addon_dir = os.path.dirname(__file__)
        blend_filename = "U3D.blend"
        object_name = "Wide_Window_Frame"
        load_object_from_blend(addon_dir, blend_filename, object_name)
        return {'FINISHED'}

class OBJECT_OT_add_wide_Window_from_blend(Operator):
    """Mall Window 5X5"""
    bl_idname = "mesh.add_window_wide_from_blend"
    bl_label = "Wide Window"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        addon_dir = os.path.dirname(__file__)
        blend_filename = "U3D.blend"
        object_name = "Wide_Window"
        load_object_from_blend(addon_dir, blend_filename, object_name)
        return {'FINISHED'}

class OBJECT_OT_add_Small_Window_frame_from_blend(Operator):
    """Mall Window 5X5"""
    bl_idname = "mesh.add_window_small_frame_from_blend"
    bl_label = "Small Window Frame"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        addon_dir = os.path.dirname(__file__)
        blend_filename = "U3D.blend"
        object_name = "Small_Window_Frame"
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

class OBJECT_MT_add_object_menu_windows(Menu):
    bl_label = "U3 Windows"
    bl_idname = "OBJECT_MT_add_object_menu_windows"

    def draw(self, context):
        layout = self.layout
        layout.operator(OBJECT_OT_add_normal_Window_from_blend.bl_idname, icon_value=custom_icons["custom_icon"].icon_id)
        layout.operator(OBJECT_OT_add_wide_Window_from_blend.bl_idname, icon_value=custom_icons["custom_icon2"].icon_id)
        layout.operator(OBJECT_OT_add_Eastern_Window_from_blend.bl_idname, icon_value=custom_icons["custom_icon2"].icon_id)
        layout.operator(OBJECT_OT_add_Small_Window_from_blend.bl_idname, icon_value=custom_icons["custom_icon2"].icon_id)
        layout.operator(OBJECT_OT_add_Window_Circle_t_from_blend.bl_idname, icon_value=custom_icons["custom_icon2"].icon_id)
        layout.operator(OBJECT_OT_add_Window_Vent_from_blend.bl_idname, icon_value=custom_icons["custom_icon2"].icon_id)
        
        layout.operator(OBJECT_OT_add_window_frame_from_blend.bl_idname, icon_value=custom_icons["custom_icon3"].icon_id)

        layout.operator(OBJECT_OT_add_wide_Window_frame_from_blend.bl_idname, icon_value=custom_icons["custom_icon2"].icon_id)
        
        layout.operator(OBJECT_OT_add_Eastern_Window_Frame_from_blend.bl_idname, icon_value=custom_icons["custom_icon2"].icon_id)
        layout.operator(OBJECT_OT_add_Small_Window_frame_from_blend.bl_idname, icon_value=custom_icons["custom_icon3"].icon_id)
        layout.operator(OBJECT_OT_add_Window_Circle_frame_from_blend.bl_idname, icon_value=custom_icons["custom_icon3"].icon_id)
        layout.operator(OBJECT_OT_add_Window_Vent_Frame_from_blend.bl_idname, icon_value=custom_icons["custom_icon2"].icon_id)

        layout.operator(OBJECT_OT_add_Mall_Window_from_blend.bl_idname, icon_value=custom_icons["custom_icon2"].icon_id)


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
    layout.menu("OBJECT_MT_add_object_menu_windows", icon_value=custom_icons["custom_icon"].icon_id)

classes = (
    OBJECT_OT_add_normal_Window_from_blend,
    OBJECT_OT_add_Mall_Window_from_blend,
    OBJECT_OT_add_Eastern_Window_from_blend,
    OBJECT_OT_add_Eastern_Window_Frame_from_blend,
    OBJECT_OT_add_Window_Vent_from_blend,
    OBJECT_OT_add_Window_Circle_t_from_blend,
    OBJECT_OT_add_Window_Vent_Frame_from_blend,
    OBJECT_OT_add_Window_Circle_frame_from_blend,
    OBJECT_OT_add_Small_Window_from_blend,
    OBJECT_OT_add_wide_Window_from_blend,
    OBJECT_OT_add_window_frame_from_blend,
    OBJECT_OT_add_Small_Window_frame_from_blend,
    OBJECT_MT_add_object_menu_windows
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    global custom_icons
    custom_icons = previews.new()
    icon_file = os.path.join(os.path.dirname(__file__), "icons", "Window.png")
    custom_icons.load("custom_icon", icon_file, 'IMAGE')
    
    icon_file2 = os.path.join(os.path.dirname(__file__), "icons", "Mall Window.png")
    custom_icons.load("custom_icon2", icon_file2, 'IMAGE')
    
    icon_file3 = os.path.join(os.path.dirname(__file__), "icons", "WindowFrame.png")
    custom_icons.load("custom_icon3", icon_file3, 'IMAGE')

    bpy.types.VIEW3D_MT_mesh_add.append(add_object_menu)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    global custom_icons
    previews.remove(custom_icons)
    bpy.types.VIEW3D_MT_mesh_add.remove(add_object_menu)

if __name__ == "__main__":
    register()
