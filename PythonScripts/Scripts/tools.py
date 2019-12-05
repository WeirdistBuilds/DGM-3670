import maya.cmds as cmds


def select_all():
    cmds.select(all=True)
    sels = cmds.ls(sl=True)
    return sels


def ball():
    obj = cmds.polySphere(name='Ball_Geo')[0]
    return obj
