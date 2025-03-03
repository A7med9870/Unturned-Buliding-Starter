import bpy

# Define the main pie menu
class OBJECT_MT_main_pie(bpy.types.Menu):
    bl_label = "Main Pie Menu"
    bl_idname = "OBJECT_MT_main_pie"


    def draw(self, context):
        layout = self.layout
        # preferences = context.preferences.addons[__name__].preferences
        preferences = bpy.context.preferences.addons['Unturned-Buliding-Starter-main'].preferences

        pie = layout.menu_pie()
        # if preferences.Geo_test:
        pie.operator("wm.call_menu_pie", text="Walls").name = "OBJECT_MT_walls_sub_pie"
        pie.operator("wm.call_menu_pie", text="Floors", icon='MESH_PLANE').name = "OBJECT_MT_floors_sub_pie"
        pie.operator("wm.call_menu_pie", text="Doors", icon='MESH_CUBE').name = "OBJECT_MT_doors_sub_pie"
        pie.operator("wm.call_menu_pie", text="Windows", icon='MESH_CUBE').name = "OBJECT_MT_windows_sub_pie"
        pie.operator("wm.call_menu_pie", text="Frames", icon='MESH_CUBE').name = "OBJECT_MT_frames_sub_pie"
        pie.operator("wm.call_menu_pie", text="Roofs", icon='MESH_CUBE').name = "OBJECT_MT_roofs_sub_pie"
        # pie.operator("view3d.view_selected", text="Frame Selected", icon='ZOOM_SELECTED')
        pie.operator("wm.call_menu_pie", text="Ramparts", icon='MESH_CUBE').name = "OBJECT_MT_ramparts_sub_pie"
        pie.operator("wm.call_menu_pie", text="Stairs", icon='MESH_CUBE').name = "OBJECT_MT_Stairs_sub_pie"

        # This is the true fucker, only worked when i had to keep look back and fourth into the main add-on loader fire
        # i fucking hate this

        # if preferences.Geo_test:
        #     pie.operator("wm.toggle_geo_test", text="No", icon='ZOOM_SELECTED')
        # else:
        #     pie.operator("wm.toggle_geo_test", text="Yeah", icon='ZOOM_SELECTED')

# Define the sub pie menu for Walls
class OBJECT_MT_walls_sub_pie(bpy.types.Menu):
    bl_label = "Walls Actions"
    bl_idname = "OBJECT_MT_walls_sub_pie"

    def draw(self, context):
        layout = self.layout

        pie = layout.menu_pie()
        pie.operator("mesh.primitive_cube_add", text="Spawn Cube", icon='MESH_CUBE')
        # Add more actions here later

# Define the sub pie menu for Floors
class OBJECT_MT_floors_sub_pie(bpy.types.Menu):
    bl_label = "Floors Actions"
    bl_idname = "OBJECT_MT_floors_sub_pie"

    def draw(self, context):
        layout = self.layout

        pie = layout.menu_pie()
        pie.operator("mesh.add_normal_floor_from_blend", text="Normal Floor", icon='MESH_CUBE') #Fucking finaly fixed
        pie.operator("mesh.add_normal_floor_only_from_blend", text="Floor only", icon='MESH_CUBE') #This is fucking confusing
        pie.operator("mesh.add_normal_floor_door_cover_from_blend", text="Floor's door cover", icon='MESH_CUBE')

# Define the sub pie menu for Doors
class OBJECT_MT_doors_sub_pie(bpy.types.Menu):
    bl_label = "Doors Actions"
    bl_idname = "OBJECT_MT_doors_sub_pie"

    def draw(self, context):
        layout = self.layout

        pie = layout.menu_pie()
        pie.operator("mesh.add_garage_door_from_blend", text="Garage Door", icon='MESH_CUBE')
        pie.operator("mesh.add_door_from_blend", text="Door", icon='MESH_CUBE')
        pie.operator("mesh.add_elevator_door_from_blend", text="Elevator door", icon='MESH_CUBE')
        pie.operator("mesh.add_door_frame_from_blend", text="Door Frame", icon='MESH_CUBE')
        pie.operator("mesh.add_door_garage_frame_from_blend", text="Garage Door Frame", icon='MESH_CUBE')
        pie.operator("mesh.add_door_eve_frame_from_blend", text="Elevator Door Frame", icon='MESH_CUBE')
        # Add more actions here later

# Define the sub pie menu for Windows
class OBJECT_MT_windows_sub_pie(bpy.types.Menu):
    bl_label = "Windows Actions"
    bl_idname = "OBJECT_MT_windows_sub_pie"

    def draw(self, context):
        layout = self.layout

        pie = layout.menu_pie()
        pie.operator("mesh.add_normal_window_from_blend", text="A Window", icon='MESH_CUBE')
        pie.operator("mesh.add_window_wide_from_blend", text="Wide Window", icon='MESH_CUBE')
        pie.operator("mesh.add_eastern_window_from_blend", text="Eastern Window", icon='MESH_CUBE')
        pie.operator("mesh.add_window_small_from_blend", text="Small Window", icon='MESH_CUBE')
        pie.operator("mesh.add_window_circlue_from_blend", text="Circle window", icon='MESH_CUBE')
        pie.operator("mesh.add_window_vent_from_blend", text="Window vent", icon='MESH_CUBE')
        pie.operator("mesh.add_window_a_frame_from_blend", text="Window vent", icon='MESH_CUBE')
        pie.operator("mesh.add_window_wide_frame_from_blend", text="Wide Window Frame", icon='MESH_CUBE')
        pie.operator("mesh.add_eastern_window_frame_from_blend", text="Eastern Window Frame", icon='MESH_CUBE')
        pie.operator("mesh.add_window_small_frame_from_blend", text="Small Window Frame", icon='MESH_CUBE')
        pie.operator("mesh.add_window_circlue_frame_blend", text="Circle_window_frame", icon='MESH_CUBE')
        pie.operator("mesh.add_window_vent_frame_from_blend", text="Window Vent Frame", icon='MESH_CUBE')
        pie.operator("mesh.add_mall_window_from_blend", text="Mall Window", icon='MESH_CUBE')
        # Add more actions here later

# Define the sub pie menu for Frames
class OBJECT_MT_frames_sub_pie(bpy.types.Menu):
    bl_label = "Frames Actions"
    bl_idname = "OBJECT_MT_frames_sub_pie"

    def draw(self, context):
        layout = self.layout

        pie = layout.menu_pie()
        pie.operator("mesh.primitive_cube_add", text="Spawn Cube", icon='MESH_CUBE')
        # Add more actions here later

# Define the sub pie menu for Roofs
class OBJECT_MT_roofs_sub_pie(bpy.types.Menu):
    bl_label = "Roofs Actions"
    bl_idname = "OBJECT_MT_roofs_sub_pie"

    def draw(self, context):
        layout = self.layout

        pie = layout.menu_pie()
        pie.operator("mesh.add_normal_roofup_from_blend", text="Roof", icon='MESH_CUBE')
        pie.operator("mesh.add_normal_rooftri_from_blend", text="Roof Tri", icon='MESH_CUBE')
        # Add more actions here later
        #

class OBJECT_MT_ramparts_sub_pie(bpy.types.Menu):
    bl_label = "Ramparts Actions"
    bl_idname = "OBJECT_MT_ramparts_sub_pie"

    def draw(self, context):
        layout = self.layout

        pie = layout.menu_pie()
        pie.operator("mesh.add_rampart_railing_from_blend", text="Rampart with railing", icon='MESH_CUBE')
        pie.operator("mesh.add_rampart_from_blend", text="Rampart", icon='MESH_CUBE')
        pie.operator("mesh.add_z_rampart_stairs_from_blend", text="Z Rampart Stairs", icon='MESH_CUBE')
        # Add more actions here later

# Stairs menu
class OBJECT_MT_Stairs_sub_pie(bpy.types.Menu):
    bl_label = "Stairs Actions"
    bl_idname = "OBJECT_MT_Stairs_sub_pie"

    def draw(self, context):
        layout = self.layout

        pie = layout.menu_pie()
        pie.operator("mesh.add_corner_stairs_from_blend", text="Corner Stairs", icon='MESH_CUBE')
        pie.operator("mesh.add_normal_stairs_from_blend", text="Stairs", icon='MESH_CUBE')
        pie.operator("mesh.add_normal_ramp_from_blend", text="Ramp", icon='MESH_CUBE')
        pie.operator("mesh.add_long_ramp_from_blend", text="Long Ramp", icon='MESH_CUBE')
        pie.operator("mesh.add_long_stairs_from_blend", text="Long Stairs", icon='MESH_CUBE')
        # Add more actions here later

# Define the keymap
addon_keymaps = []

def register():
    bpy.utils.register_class(OBJECT_MT_main_pie)
    bpy.utils.register_class(OBJECT_MT_walls_sub_pie)
    bpy.utils.register_class(OBJECT_MT_floors_sub_pie)
    bpy.utils.register_class(OBJECT_MT_doors_sub_pie)
    bpy.utils.register_class(OBJECT_MT_windows_sub_pie)
    bpy.utils.register_class(OBJECT_MT_frames_sub_pie)
    bpy.utils.register_class(OBJECT_MT_roofs_sub_pie)
    bpy.utils.register_class(OBJECT_MT_ramparts_sub_pie)
    bpy.utils.register_class(OBJECT_MT_Stairs_sub_pie)

    # Add keymap
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')
    kmi = km.keymap_items.new("wm.call_menu_pie", 'Q', 'PRESS')
    kmi.properties.name = "OBJECT_MT_main_pie"
    addon_keymaps.append((km, kmi))

def unregister():
    bpy.utils.unregister_class(OBJECT_MT_main_pie)
    bpy.utils.unregister_class(OBJECT_MT_walls_sub_pie)
    bpy.utils.unregister_class(OBJECT_MT_floors_sub_pie)
    bpy.utils.unregister_class(OBJECT_MT_doors_sub_pie)
    bpy.utils.unregister_class(OBJECT_MT_windows_sub_pie)
    bpy.utils.unregister_class(OBJECT_MT_frames_sub_pie)
    bpy.utils.unregister_class(OBJECT_MT_roofs_sub_pie)
    bpy.utils.unregister_class(OBJECT_MT_ramparts_sub_pie)
    bpy.utils.unregister_class(OBJECT_MT_Stairs_sub_pie)

    # Remove keymap
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

if __name__ == "__main__":
    register()
