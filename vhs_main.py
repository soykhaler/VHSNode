bl_info = {
    "name": "VHS Node",
    "author": "SoyKhaler",
    "version": (1, 0),
    "blender": (3, 0, 0),
    "location": "Compositing Tab",
    "description": "Create a VHS editable Node for your renders",
    "category": "Import-Export",
}

import bpy
from bpy.app.handlers import persistent
import os

@persistent
def load_handler_vhs(dummy):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir, 'vhs.blend')
    
    if os.path.exists(filepath):
        with bpy.data.libraries.load(filepath) as (data_from, data_to):
            data_to.node_groups = [name for name in data_from.node_groups if name == 'VHS']

        for node_group in data_to.node_groups:
            if node_group is not None:
                bpy.data.node_groups[node_group.name] = node_group

def register():
    bpy.app.handlers.load_post.append(load_handler_vhs)

def unregister():
    bpy.app.handlers.load_post.remove(load_handler_vhs)

if __name__ == "__main__":
    register()
