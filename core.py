from maya import cmds

def auto_unwrap():
    newchain = cmds.ls(sl=True)

    for obj in newchain:
        cmds.polyAutoProjection(obj)
        cmds.u3dLayout(obj)
        cmds.polySetToFaceNormal
        cmds.polySoftEdge(a=45)
        cmds.delete(ch=True)
        cmds.makeIdentity(a=True)