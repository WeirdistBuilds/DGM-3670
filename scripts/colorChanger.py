import maya.cmds as cmds


def color_changer(color):
    this_color = {
        'yellow': lambda: 17,
        'red': lambda: 13,
        'blue': lambda: 6,
        'green': lambda: 19,
        'purple': lambda: 30,
        'orange': lambda: 12,
        'black': lambda: 1,
        'white': lambda: 16
    }.get(color, lambda: 5)()

    selection = cmds.ls(sl=True)
    shapes = cmds.listRelatives(selection, shapes=True, children=True)
    for shape in shapes:
        cmds.setAttr('%s.overrideEnabled' % shape, True)
        cmds.setAttr('%s.overrideColor' % shape, this_color)
