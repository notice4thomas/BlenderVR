import bpy
from .. import blendervr
from .. import developer_utils as dutil


# Operator to connect to the server and start broadcasting to the HMD
class ActivateHMD(bpy.types.Operator):
    bl_idname = "vr.activate"
    bl_label = "Start VR"
    bl_options = {'REGISTER'}

    def execute(self, context):
        dutil.deb("Starting VR!")
        blendervr.getServer().start()
        return {'FINISHED'}
