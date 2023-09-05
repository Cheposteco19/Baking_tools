from maya import cmds
from uv_testing_tool import ui

def low_exportFBX(fileName, fileType):
    cmds.file(fileName);
    return 1