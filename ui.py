from maya import cmds

WINDOW_NAME='uv_test_tool_ui'
CHECK_BOX_NAME='auto-unwrap_check_box'
LOW_POLY_PATH_TEXT_BOX_NAME='low_poly_path_text_box'
HIGH_POLY_PATH_TEXT_BOX_NAME='high_poly_path_text_box'

def show_ui():
    # Delete old window
    if cmds.window(WINDOW_NAME, exists=True,query=True):
        cmds.deleteUI(WINDOW_NAME)

    # Create new window
    cmds.window(WINDOW_NAME, title='UV Testing Tool', widthHeight=(450,100))

    #Auto-Unwrap
    cmds.columnLayout(adj=True)
    cmds.checkBox(CHECK_BOX_NAME,label="Auto-Unwrap")

    # Browse Low Button
    cmds.rowLayout(numberOfColumns=4)
    #cmds.textFieldButtonGrp(bl="...", bc=browse, fi=LOW_POLY_PATH_TEXT_BOX_NAME, l="Export Low Resolution")
    cmds.text(l='Export Low Resolution')
    cmds.textField(LOW_POLY_PATH_TEXT_BOX_NAME)
    cmds.button(l='...')
    cmds.button(l='Export')
    cmds.setParent('..')
    cmds.rowLayout(numberOfColumns=4)
    #cmds.textFieldButtonGrp(bl="...", bc=browse, fi=HI_POLY_PATH_TEXT_BOX_NAME, l="Export High Resolution")
    cmds.text(l='Export Low Resolution')
    cmds.textField(HIGH_POLY_PATH_TEXT_BOX_NAME)
    cmds.button(l='...')
    cmds.button(l='Export')
    cmds.setParent('..')
    cmds.text(l='GD67_JoseMunguia', al='right')

    # Show window
    cmds.showWindow()

def exportFBX(fileName, fileType):
    cmds.file(fileName, i=True);
    return 1

    # Browse defined
def browse():
    address = cmds.fileDialog2(ff="FBX", ds=2)
    print