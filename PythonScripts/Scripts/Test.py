import maya.cmds as cmds

cmds.polySphere(axis=[1, 0, 0], radius=5, name='Ball', constructionHistory=True)
cmds.polyCube(d=5, w=3, h=4, n='Box')