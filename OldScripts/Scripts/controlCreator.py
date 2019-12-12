import maya.cmds as cmds


def control_creator(self, color):
    """
    Creates control circle on selected objects
    input: string (yellow, red, blue, green, purple, orange, black, or white)
    return: none
    """
    objects = center_locator(True, True)
    for obj in objects:
        split_name = obj.split('_')
        split_name.pop(len(split_name) - 1)
        new_name = ''
        for word in split_name:
            new_name += '%s_' % word
        new_name += '_Ctrl'
        grp_name = '%s_Grp' % new_name
        cmds.circle(name=new_name)
        color_changer(color)
        position = cmds.xform(obj, q=True, ws=True, rp=True)
        cmds.xform(new_name, ws=True, t=position)
        cmds.group(empty=True, name=grp_name)
        cmds.parent(new_name, grp_name)
