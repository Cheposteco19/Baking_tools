from maya import cmds
import maya.mel as mm

def auto_unwrap():
    selected_items = cmds.ls(sl=True)

    for item in selected_items:
        cmds.polyAutoProjection(item)

    cmds.u3dLayout(item)

    for item in selected_items:
        cmds.polySetToFaceNormal(item)
        mm.eval('polyUVBorderHard;')
        cmds.DeleteHistory(item)
        cmds.FreezeTransformations()