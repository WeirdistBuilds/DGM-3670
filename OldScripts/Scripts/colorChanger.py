import maya.cmds as cmds


def color_changer(color):
    this_color = {
        'yellow': lambda: 16,
        'red': lambda: 12,
        'blue': lambda: 5,
        'green': lambda: 13,
        'purple': lambda: 7,
        'orange': lambda: 11,
        'black': lambda: 1,
        'white': lambda: 15
    }.get(color, lambda: 6)()

    selection = cmds.ls(sl=True)
    shapes = cmds.listRelatives(selection, shapes=True, children=True)
    for shape in shapes:
        cmds.setAttr('%s.overrideEnabled' % shape, True)
        cmds.setAttr('%s.overrideColor' % shape, this_color)
