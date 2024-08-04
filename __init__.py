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
from . import Stairs
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
        default="https://github.com/A7med9870/Unturned-Buliding-Starter",
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
        default=False,
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
    Geo_test: bpy.props.BoolProperty(
        name="Don't Center Geometery frame",
        description="Will import frames with the origin being the center, turning it on; will make frame meshes show up in the center of the cursor",
        default=False,
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
    show_stairs_objects_panel: bpy.props.BoolProperty(
        name="Stairs",
        description="Toggle visibility of Stairs meshs",
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
        row.prop(self, "show_ramparts_objects_panel")
        row.prop(self, "show_stairs_objects_panel")

        row = layout.row()
        row.prop(self, "Geo_test")

        row = layout.row()
        row.operator("wm.url_open", text="Github Page").url = self.documentation_url
        row.operator("wm.url_open", text="Creator's Youtube").url = self.YT_url
        row.operator("wm.url_open", text="Creator's Instagram").url = self.IG_url

        layout.label(text="Thanks for trying out the addon!")
    def invoke(self, context, event):
        import webbrowser
        webbrowser.open(self.documentation_url)
        return {'FINISHED'}

class OBJECT_OT_toggle_geo_test(Operator):
    """Toggle Geo Test"""
    bl_idname = "wm.toggle_geo_test"
    bl_label = "Toggle Geo Test"

    def execute(self, context):
        preferences = bpy.context.preferences.addons['Unturned-Buliding-Starter-main'].preferences
        preferences.Geo_test = not preferences.Geo_test
        self.report({'INFO'}, f"Geo Test set to {preferences.Geo_test}")
        return {'FINISHED'}

class VIEW3D_PT_unturned_settings(Panel):
    bl_label = "Unturned Buildings Starter Settings"
    bl_idname = "VIEW3D_PT_unturned_settings"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'UBS_S'

    def draw(self, context):
        layout = self.layout
        preferences = context.preferences.addons[__name__].preferences

        layout.prop(preferences, "Geo_test")
        row = layout.row()
        #if preferences.show_Export_panel: #disaled as this menu is just aint ready to be lannched
        #    row.prop(preferences, "show_Export_panel", text="", icon_value=custom_icons["custom_icon"].icon_id)
        #else:
        #    row.prop(preferences, "show_Export_panel", text="", icon_value=custom_icons["custom_icon2"].icon_id)
        #row.prop(preferences, "show_Extra_objects_panel")
        if preferences.show_Floors_objects_panel:
            row.prop(preferences, "show_Floors_objects_panel", text="", icon_value=custom_icons["custom_icon13"].icon_id)
        else:
            row.prop(preferences, "show_Floors_objects_panel", text="", icon_value=custom_icons["custom_icon13"].icon_id)
        if preferences.show_doors_objects_panel:
            row.prop(preferences, "show_doors_objects_panel", text="", icon_value=custom_icons["custom_icon2"].icon_id)
        else:
            row.prop(preferences, "show_doors_objects_panel", text="", icon_value=custom_icons["custom_icon2"].icon_id)
        if preferences.show_windows_objects_panel:
            row.prop(preferences, "show_windows_objects_panel", text="", icon_value=custom_icons["custom_icon7"].icon_id)
        else:
            row.prop(preferences, "show_windows_objects_panel", text="", icon_value=custom_icons["custom_icon7"].icon_id)
        if preferences.show_ramparts_objects_panel:
            row.prop(preferences, "show_ramparts_objects_panel", text="", icon_value=custom_icons["custom_icon"].icon_id)
        else:
            row.prop(preferences, "show_ramparts_objects_panel", text="", icon_value=custom_icons["custom_icon"].icon_id)
        if preferences.show_stairs_objects_panel:
            row.prop(preferences, "show_stairs_objects_panel", text="", icon_value=custom_icons["custom_icon15"].icon_id)
        else:
            row.prop(preferences, "show_stairs_objects_panel", text="", icon_value=custom_icons["custom_icon15"].icon_id)
        if preferences.show_roofs_objects_panel:
            row.prop(preferences, "show_roofs_objects_panel", text="", icon_value=custom_icons["custom_icon13"].icon_id)
        else:
            row.prop(preferences, "show_roofs_objects_panel", text="", icon_value=custom_icons["custom_icon13"].icon_id)
        if preferences.show_Extra_objects_panel:
            row.prop(preferences, "show_Extra_objects_panel", text="", icon_value=custom_icons["custom_icon"].icon_id)
        else:
            row.prop(preferences, "show_Extra_objects_panel", text="", icon_value=custom_icons["custom_icon2"].icon_id)

        #layout.operator("wm.toggle_geo_test", text="Toggle Geo Test")


def add_object_menu(self, context):
    layout = self.layout

def register():
    exy.register()
    Floors.register()
    Walls.register()
    Doors.register()
    Windows.register()
    Roofs.register()
    Ramparts.register()
    Stairs.register()
    exy_extra.register()
    bpy.utils.register_class(VIEW3D_PT_unturned_settings)
    bpy.utils.register_class(OBJECT_OT_toggle_geo_test)
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
    Stairs.unregister()
    global custom_icons
    bpy.utils.unregister_class(Settingsofwed)
    bpy.utils.unregister_class(OBJECT_OT_toggle_geo_test)
    bpy.utils.unregister_class(VIEW3D_PT_unturned_settings)

    bpy.types.VIEW3D_MT_mesh_add.remove(add_object_menu)

    previews.remove(custom_icons)

if __name__ == "__main__":
    register()
