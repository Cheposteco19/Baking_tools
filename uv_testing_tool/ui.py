from uv_testing_tool import core
from maya import cmds

WINDOW_NAME='uv_test_tool_ui'
CHECK_BOX_NAME='auto_unwrap_check_box'
LOW_POLY_PATH_TEXT_BOX_NAME='low_poly_path_text_box'
HIGH_POLY_PATH_TEXT_BOX_NAME='high_poly_path_text_box'

def show_ui():
    # Delete old window
    if cmds.window(WINDOW_NAME, exists=True,query=True):
        cmds.deleteUI(WINDOW_NAME)

    # Create new window
    cmds.window(WINDOW_NAME, title='UV Testing Tool', widthHeight=(500,100))

    #Auto-Unwrap
    cmds.columnLayout(adjustableColumn=True)
    cmds.checkBox(CHECK_BOX_NAME,label="Auto-Unwrap")

    # Browse Low Export
    cmds.rowLayout(numberOfColumns=4)
    cmds.text(label='Export Low Resolution')
    cmds.textField(LOW_POLY_PATH_TEXT_BOX_NAME,width=304)
    cmds.button(label='...',command=browse_low)
    cmds.button(label='Export',command=low_exportFBX)
    cmds.setParent('..')

    # Browse High Export
    cmds.rowLayout(numberOfColumns=4)
    cmds.text(label='Export High Resolution')
    cmds.textField(HIGH_POLY_PATH_TEXT_BOX_NAME,width=300)
    cmds.button(label='...',command=browse_high)
    cmds.button(label='Export',command=high_exportFBX)
    cmds.setParent('..')

    #Credits
    cmds.text(label='GD67_JoseMunguia', align='right')

    # Show window
    cmds.showWindow()

    # Browse defined
def browse_low(*args):
    low_path = cmds.fileDialog2(fileFilter="*.fbx", dialogStyle=2)
    cmds.textField(LOW_POLY_PATH_TEXT_BOX_NAME,edit=True,text=low_path[0])

def browse_high(*args):
    high_path = cmds.fileDialog2(fileFilter="*.fbx", dialogStyle=2)
    cmds.textField(HIGH_POLY_PATH_TEXT_BOX_NAME,edit=True,text=high_path[0])

#Export buttons
def low_exportFBX(*args):
    if cmds.checkBox(CHECK_BOX_NAME,query=True,value=True)==True:
        core.auto_unwrap()
    low_path = cmds.textField(LOW_POLY_PATH_TEXT_BOX_NAME, query=True, text=True)
    cmds.file(low_path,force=True,options='v=0;',type='FBX export',exportSelected=True,preserveReferences=True)

def high_exportFBX(*args):
    high_path = cmds.textField(HIGH_POLY_PATH_TEXT_BOX_NAME, query=True, text=True)
    cmds.file(high_path,force=True,options='v=0;',type='FBX export',exportSelected=True,preserveReferences=True)
