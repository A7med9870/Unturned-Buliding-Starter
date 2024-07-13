import bpy
import bmesh
import webbrowser
from mathutils import Vector
from bpy.props import (StringProperty, PointerProperty, EnumProperty, BoolProperty)
from bpy.types import (Panel, Operator, AddonPreferences, PropertyGroup)

class MySettings(PropertyGroup):

    path: StringProperty(
        description="Path to Directory",
        maxlen=1024,
        subtype='FILE_PATH')



    apply_origin: BoolProperty(
        name="Export Object's Origin?",
        description="Whether to use the object's origin as the export origin",
        default=False
    )

class hamada_unturnned_PanelExportAll(bpy.types.Panel):
    bl_label = "Export panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Export_to_Unturned"
    bl_context = "objectmode"
    bl_order = 7

    @classmethod
    def poll(cls, context):
        preferences = bpy.context.preferences.addons['Unturned-Buliding-Starter-main'].preferences
        return preferences.show_Export_panel
    def draw(self, context):
        layout = self.layout
        scn = context.scene
        layout.label(text="Export Path Location:")
        layout.prop(scn.my_tool, "path", text="")
        layout.label(text="Don't forget to UNCHECK RELATIVE PATH")
        layout.operator("myops.batch_exporter", text='Export Separate', icon='TRIA_RIGHT')
        layout.operator("myops.export_zero_pos", text='Export Separate at Zero Position', icon='TRIA_RIGHT')
        layout.operator("myops.combined_exporter", text='Export Combined', icon='TRIA_RIGHT')
        #layout.operator("myops.combined_export_zero_pos", text='Export Combined at Zero Position', icon='TRIA_RIGHT')

class hamada_unturnned_BatchExportE(bpy.types.Operator):
    bl_idname = "myops.batch_exporter"
    bl_label = "Export Selected"
    bl_options = {"UNDO"}

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        hamada_unturnned_export_all(context.scene.my_tool.path)
        self.report({'INFO'}, 'ExportedBatchExport')
        return {'FINISHED'}

class hamada_unturnned_ExportZeroPosE(bpy.types.Operator):
    bl_idname = "myops.export_zero_pos"
    bl_label = "Export Selected at Zero Position"
    bl_options = {"UNDO"}

    def execute(self, context):
        objects = context.selected_objects
        for obj in objects:
            obj.location = (0, 0, 0)
        hamada_unturnned_export_all(context.scene.my_tool.path)
        self.report({'INFO'}, 'Exported at Zero Position')
        return {'FINISHED'}

class hamada_unturnned_MyUnitScale(bpy.types.Operator):
    """Sets the scale of world to correct scale to export to unreal"""
    bl_idname = "my_operator.my_unitscale_operator"
    bl_label = "Set Unit Scale"

    def execute(self, context):
        bpy.context.scene.unit_settings.scale_length = 0.01
        return {'FINISHED'}

class hamada_unturnned_CombinedExporterE(bpy.types.Operator):
    bl_idname = "myops.combined_exporter"
    bl_label = "Export Combined"
    bl_options = {"UNDO"}

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        hamada_unturnned_export_combined(context.scene.my_tool.path)
        self.report({'INFO'}, 'Exported Combined')
        return {'FINISHED'}

class Combinedhamada_unturnned_ExportZeroPosE(bpy.types.Operator):
    bl_idname = "myops.combined_export_zero_pos"
    bl_label = "Export Combined at Zero Position"
    bl_options = {"UNDO"}

    def execute(self, context):
        objects = context.selected_objects
        for obj in objects:
            obj.location = (0, 0, 0)
        hamada_unturnned_export_combined(context.scene.my_tool.path)
        self.report({'INFO'}, 'Exported Combined at Zero Position')
        return {'FINISHED'}

def hamada_unturnned_export_combined(export_folder):
    objects = bpy.context.selected_objectsX
    orig_locs = []

    for obj in objects:
        orig_locs.append(obj.location.copy())
        obj.name = obj.name

    export_name = export_folder + bpy.context.active_object.name + '.fbx'
    bpy.ops.export_scene.fbx(filepath=export_name, use_selection=True, mesh_smooth_type='FACE')

    for obj in objects:
        obj.location = orig_locs.pop(0)


def hamada_unturnned_export_combinedZero(export_folder):
    objects = bpy.context.selected_objects
    orig_locs = []

    for obj in objects:
        orig_locs.append(obj.location.copy())
        obj.location = (0.0, 0.0, 0.0)
        obj.name = obj.name

    export_name = export_folder + bpy.context.active_object.name + '.fbx'
    bpy.ops.export_scene.fbx(filepath=export_name, use_selection=True, mesh_smooth_type='FACE')

    for obj in objects:
        obj.location = orig_locs.pop(0)

def hamada_unturnned_export_all(export_folder):
    objects = bpy.context.selected_objects
    for obj in objects:
        bpy.ops.object.select_all(action='DESELECT')
        obj.select_set(True)
        if obj.type not in ['MESH']:
            continue
        export_name = export_folder + obj.name + '.fbx'
        bpy.ops.export_scene.fbx(filepath=export_name, use_selection=True, mesh_smooth_type='FACE')

def hamada_unturnned_export_allZero(export_folder):
    objects = bpy.context.selected_objects
    for obj in objects:
        bpy.ops.object.select_all(action='DESELECT')
        obj.select_set(True)
        if obj.type not in ['MESH']:
            continue
        obj.location = (0, 0, 0)
        export_name = export_folder + obj.name + '.fbx'
        bpy.ops.export_scene.fbx(filepath=export_name, use_selection=True, mesh_smooth_type='FACE')


classes = (
    hamada_unturnned_PanelExportAll,
    hamada_unturnned_BatchExportE,
    hamada_unturnned_CombinedExporterE,
    hamada_unturnned_ExportZeroPosE,
    Combinedhamada_unturnned_ExportZeroPosE,
    MySettings,
    hamada_unturnned_MyUnitScale
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.my_tool = bpy.props.PointerProperty(type=MySettings)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.my_tool

if __name__ == "__main__":
    register()
