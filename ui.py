from maya import cmds
from uv_testing_tool import core

WINDOW_NAME='uv_test_tool_ui'
CHECK_BOX_NAME='auto-unwrap_check_box'
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
    cmds.textField(LOW_POLY_PATH_TEXT_BOX_NAME,width=300)
    cmds.button(label='...',command=browse_low)
    cmds.button(label='Export',command=browse_low)
    cmds.setParent('..')

    # Browse High Export
    cmds.rowLayout(numberOfColumns=4)
    cmds.text(label='Export Low Resolution')
    cmds.textField(HIGH_POLY_PATH_TEXT_BOX_NAME,width=300)
    cmds.button(label='...')
    cmds.button(label='Export')
    cmds.setParent('..')

    #Credits
    cmds.text(label='GD67_JoseMunguia', align='right')

    # Show window
    cmds.showWindow()

    # Browse defined
def browse_low(*args):
    path = cmds.fileDialog2(fileFilter="FBX", dialogStyle=2)
    cmds.textField(LOW_POLY_PATH_TEXT_BOX_NAME,edit=True,text=path[0])

def browse_high(*args):
    path = cmds.fileDialog2(fileFilter="FBX", dialogStyle=2)
    cmds.textField(HIGH_POLY_PATH_TEXT_BOX_NAME,edit=True,text=path[0])