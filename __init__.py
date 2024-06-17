bl_info = {
    "name": "Unturned Buildings Starter",
    "author": "A7med9870",
    "version": (1, 0),
    "blender": (4, 1, 0),
    "location": "View3D > Add > Mesh > Add Object from Blend File",
    "description": "Adds your desired Unturned style building model to the scene",
    "warning": "",
    "doc_url": "",
    "category": "Add Mesh",
}

import bpy
import os
from bpy.types import Operator, Menu
from bpy.utils import previews
from mathutils import Quaternion
from bpy.types import Panel, AddonPreferences
from bpy.props import BoolProperty, EnumProperty
from . import exy
from . import Floors
from . import exy_extra
from . import Walls
from . import Doors
from . import Windows
from . import Roofs
from . import Ramparts
# Directory for the add-on
icon_dir = os.path.join(os.path.dirname(__file__), "icons")

# Custom icon previews
custom_icons = None

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
#options menu
class Settingsofwed(bpy.types.AddonPreferences):
    bl_idname = __name__

    documentation_url: bpy.props.StringProperty(
        name="Documentation URL",
        description="URL for the addon documentation",
        default="https://github.com/A7med9870/Blender-Car-Streamliner",
    )
    YT_url: bpy.props.StringProperty(
        name="YT URL",
        description="URL for the Creator Youtube",
        default="https://www.youtube.com/channel/UCMbA857nJ9w5FzfjrhBzq8A",
    )
    IG_url: bpy.props.StringProperty(
        name="IG URL",
        description="URL for the Creator Instagram",
        default="https://www.instagram.com/a7hmed9870/reels/?hl=en",
    )
    Inspire_url: bpy.props.StringProperty(
        name="insipre URL",
        description="URL for the Creator that inspired this addon",
        default="https://www.instagram.com/a7hmed9870/reels/?hl=en",
    )
    show_Export_panel: bpy.props.BoolProperty(
        name="Show Export to FBX Panel",
        description="Toggle visibility of the Export to FBX Panel",
        default=True,
        update=lambda self, context: context.area.tag_redraw(),
    )
    show_Extra_objects_panel: bpy.props.BoolProperty(
        name="Extra Meshes",
        description="Toggle visibility of Extra meshs in dev",
        default=True,
        update=lambda self, context: context.area.tag_redraw(),
    )
    show_Floors_objects_panel: bpy.props.BoolProperty(
        name="Floors",
        description="Toggle visibility of Floors meshs",
        default=True,
        update=lambda self, context: context.area.tag_redraw(),
    )
    show_Walls_objects_panel: bpy.props.BoolProperty(
        name="Walls",
        description="Toggle visibility of Walls meshs",
        default=True,
        update=lambda self, context: context.area.tag_redraw(),
    )
    show_doors_objects_panel: bpy.props.BoolProperty(
        name="Doors",
        description="Toggle visibility of Doors meshs",
        default=True,
        update=lambda self, context: context.area.tag_redraw(),
    )
    show_windows_objects_panel: bpy.props.BoolProperty(
        name="Windows",
        description="Toggle visibility of Window meshs",
        default=True,
        update=lambda self, context: context.area.tag_redraw(),
    )
    show_roofs_objects_panel: bpy.props.BoolProperty(
        name="Roofs",
        description="Toggle visibility of Roofs meshs",
        default=True,
        update=lambda self, context: context.area.tag_redraw(),
    )
    show_ramparts_objects_panel: bpy.props.BoolProperty(
        name="Ramparts",
        description="Toggle visibility of Ramparts meshs",
        default=True,
        update=lambda self, context: context.area.tag_redraw(),
    )

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "Boners_enum1")

        #row = layout.row()
        #row.prop(self, "show_shapekeylist_panel")
        row = layout.row()
        row.prop(self, "show_Export_panel")
        row.prop(self, "show_Extra_objects_panel")
        row.label(text="wed")

        row = layout.row()
        row.prop(self, "show_Floors_objects_panel")
        row.prop(self, "show_roofs_objects_panel")
        row.prop(self, "show_doors_objects_panel")

        row = layout.row()
        row.prop(self, "show_windows_objects_panel")

        row = layout.row()
        row.operator("wm.url_open", text="Github Page").url = self.documentation_url
        row.operator("wm.url_open", text="Creator's Youtube").url = self.YT_url
        row.operator("wm.url_open", text="Creator's Instagram").url = self.IG_url

        layout.label(text="Thanks for trying out the addon!")
    def invoke(self, context, event):
        import webbrowser
        webbrowser.open(self.documentation_url)
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
    bl_idname = "mesh.add_normal_stairs_from_blend"
    bl_label = "Stairs"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        addon_dir = os.path.dirname(__file__)
        blend_filename = "U3D.blend"
        object_name = "Stairs"
        load_object_from_blend(addon_dir, blend_filename, object_name)
        return {'FINISHED'}

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

class OBJECT_MT_add_object_menu_stairs(Menu):
    bl_label = "U3 Stairs"
    bl_idname = "OBJECT_MT_add_object_menu_stairs"

    def draw(self, context):
        layout = self.layout
        layout.operator(OBJECT_OT_add_Corner_from_blend.bl_idname, icon_value=custom_icons["custom_icon16"].icon_id)
        layout.operator(OBJECT_OT_add_Stairs_from_blend.bl_idname, icon_value=custom_icons["custom_icon15"].icon_id)
        layout.operator(OBJECT_OT_add_Ramp_from_blend.bl_idname, icon_value=custom_icons["custom_icon"].icon_id)
        layout.operator(OBJECT_OT_add_LongRamp_from_blend.bl_idname, icon_value=custom_icons["custom_icon"].icon_id)
        layout.operator(OBJECT_OT_add_LongStairs_from_blend.bl_idname, icon_value=custom_icons["custom_icon"].icon_id)


def add_object_menu(self, context):
    layout = self.layout
    layout.menu("OBJECT_MT_add_object_menu_stairs", icon_value=custom_icons["custom_icon15"].icon_id)

def register():
    exy.register()
    Floors.register()
    Walls.register()
    Doors.register()
    Windows.register()
    Roofs.register()
    Ramparts.register()
    exy_extra.register()
    global custom_icons
    custom_icons = previews.new()
    icon_file = os.path.join(os.path.dirname(__file__), "icons", "custom_icon.png")
    custom_icons.load("custom_icon", icon_file, 'IMAGE')
    
    icon_file2 = os.path.join(os.path.dirname(__file__), "icons", "door.png")
    custom_icons.load("custom_icon2", icon_file2, 'IMAGE')
    
    icon_file3 = os.path.join(os.path.dirname(__file__), "icons", "garage_door.png")
    custom_icons.load("custom_icon3", icon_file3, 'IMAGE')
    
    icon_file4 = os.path.join(os.path.dirname(__file__), "icons", "Elevator Door.png")
    custom_icons.load("custom_icon4", icon_file4, 'IMAGE')
    
    icon_file5 = os.path.join(os.path.dirname(__file__), "icons", "Door Frame.png")
    custom_icons.load("custom_icon5", icon_file5, 'IMAGE')
    
    icon_file6 = os.path.join(os.path.dirname(__file__), "icons", "Garage Door Frame.png")
    custom_icons.load("custom_icon6", icon_file6, 'IMAGE')
    
    icon_file7 = os.path.join(os.path.dirname(__file__), "icons", "Window.png")
    custom_icons.load("custom_icon7", icon_file7, 'IMAGE')
    
    icon_file8 = os.path.join(os.path.dirname(__file__), "icons", "Mall Window.png")
    custom_icons.load("custom_icon8", icon_file8, 'IMAGE')
    
    icon_file9 = os.path.join(os.path.dirname(__file__), "icons", "WindowFrame.png")
    custom_icons.load("custom_icon9", icon_file9, 'IMAGE')
    
    icon_file10 = os.path.join(os.path.dirname(__file__), "icons", "Wall.png")
    custom_icons.load("custom_icon10", icon_file10, 'IMAGE')
    
    icon_file11 = os.path.join(os.path.dirname(__file__), "icons", "Corner Wall.png")
    custom_icons.load("custom_icon11", icon_file11, 'IMAGE')
    
    icon_file12 = os.path.join(os.path.dirname(__file__), "icons", "Wall_zf_corner.png")
    custom_icons.load("custom_icon12", icon_file12, 'IMAGE')
    
    icon_file13 = os.path.join(os.path.dirname(__file__), "icons", "Floor.png")
    custom_icons.load("custom_icon13", icon_file13, 'IMAGE')
    
    icon_file14 = os.path.join(os.path.dirname(__file__), "icons", "Roofup.png")
    custom_icons.load("custom_icon14", icon_file14, 'IMAGE')
    
    icon_file15 = os.path.join(os.path.dirname(__file__), "icons", "Stairs.png")
    custom_icons.load("custom_icon15", icon_file15, 'IMAGE')
    
    icon_file16 = os.path.join(os.path.dirname(__file__), "icons", "Corner Stairs.png")
    custom_icons.load("custom_icon16", icon_file16, 'IMAGE')
    
    bpy.utils.register_class(OBJECT_OT_add_LongRamp_from_blend)
    bpy.utils.register_class(OBJECT_OT_add_Ramp_from_blend)
    bpy.utils.register_class(OBJECT_OT_add_LongStairs_from_blend)
    bpy.utils.register_class(OBJECT_OT_add_Corner_from_blend)
    bpy.utils.register_class(OBJECT_OT_add_Stairs_from_blend)
    bpy.utils.register_class(OBJECT_MT_add_object_menu_stairs)
    bpy.utils.register_class(Settingsofwed)
    
    bpy.types.VIEW3D_MT_mesh_add.append(add_object_menu)
    
def unregister():
    exy.unregister()
    exy_extra.unregister()
    Floors.unregister()
    Walls.register()
    Doors.unregister()
    Windows.unregister()
    Roofs.unregister()
    Ramparts.unregister()
    global custom_icons
    bpy.utils.unregister_class(Settingsofwed)
    bpy.utils.unregister_class(OBJECT_OT_add_LongRamp_from_blend)
    bpy.utils.unregister_class(OBJECT_OT_add_Ramp_from_blend)
    bpy.utils.unregister_class(OBJECT_OT_add_LongStairs_from_blend)
    bpy.utils.unregister_class(OBJECT_OT_add_Corner_from_blend)
    bpy.utils.unregister_class(OBJECT_OT_add_Stairs_from_blend)
    bpy.utils.unregister_class(OBJECT_MT_add_object_menu_stairs)

    bpy.types.VIEW3D_MT_mesh_add.remove(add_object_menu)

    previews.remove(custom_icons)

if __name__ == "__main__":
    register()
