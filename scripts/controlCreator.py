import maya.cmds as cmds
import colorChanger as color


def control_creator(color_name):
    """
    Creates control circle on selected objects
    input: string (yellow, red, blue, green, purple, orange, black, or white)
    return: none
    """
    selection = cmds.ls(sl=True)
    controls = list()
    for sel in selection:
        split_name = sel.split('.[]_:')
        if len(split_name) >= 2:
            split_name.pop(len(split_name) - 1)
        current_name = ''
        for word in split_name:
            current_name += '%s_' % word
        current_name += 'Ctrl'
        current_position = [0, 0, 0]
        bounding_box = cmds.xform(sel, query=True, ws=True, boundingBox=True)
        current_position[0] = (bounding_box[0] + bounding_box[3]) / 2
        current_position[1] = (bounding_box[1] + bounding_box[4]) / 2
        current_position[2] = (bounding_box[2] + bounding_box[5]) / 2
        current_rotation = cmds.xform(sel, ro=True, q=True)
        cmds.circle(name=current_name)
        cmds.xform(current_name, t=(current_position[0], current_position[1], current_position[2]),
                   ro=(current_rotation[0], current_rotation[1], current_rotation[2]))
        controls.append(current_name)
        grp_name = '%s_Grp' % current_name
        cmds.group(empty=True, name=grp_name)
        cmds.xform(grp_name, t=(current_position[0], current_position[1], current_position[2]),
                   ro=(current_rotation[0], current_rotation[1], current_rotation[2]))
        cmds.parent(current_name, grp_name)
        cmds.select(controls)
        color.color_changer(color_name)
