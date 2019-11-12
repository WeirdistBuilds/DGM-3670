import maya.cmds as cmds

cmds.polySphere(radius=3, subdivisionsX=12, subdivisionsY=12, axis=[0, 1, 0], createUVs=2, constructionHistory=1, name='Bottom')
cmds.move(0, -3, 0, 'Bottom.scalePivot', 'Bottom.rotatePivot', relative=True)
cmds.move(rotatePivotRelative=True, moveY=0)

cmds.polySphere(radius=2, subdivisionsX=12, subdivisionsY=12, axis=[0, 1, 0], createUVs=2, constructionHistory=1, name='Middle')
cmds.move(0, -2, 0, 'Middle.scalePivot', 'Middle.rotatePivot', relative=True)
cmds.move(0, 7, 0, 'Middle', relative=True)

cmds.polySphere(radius=1, subdivisionsX=12, subdivisionsY=12, axis=[0, 1, 0], createUVs=2, constructionHistory=1, name='Top')
cmds.move(0, -1, 0, 'Top.scalePivot', 'Top.rotatePivot', relative=True)
cmds.move(0, 9.5, 0, 'Top', relative=True)

cmds.polyCone(radius=.2, height=2, subdivisionsX=12, subdivisionsY=1, subdivisionsZ=0, axis=[-1, 0, 0], roundCap=0, createUVs=3, constructionHistory=1, name='Carrot')
cmds.move(-1.5, 9.5, 0, 'Carrot', relative=True)

cmds.polySphere(radius=.2, subdivisionsX=6, subdivisionsY=6, axis=[0, 1, 0], createUVs=2, constructionHistory=1, name='Eye_L')
cmds.move(-0.7, 10, 0.5, 'Eye_L', relative=True)

cmds.polySphere(radius=.2, subdivisionsX=6, subdivisionsY=6, axis=[0, 1, 0], createUVs=2, constructionHistory=1, name='Eye_R')
cmds.move(-0.7, 10, -0.5, 'Eye_R', relative=True)

cmds.polySphere(radius=.2, subdivisionsX=6, subdivisionsY=6, axis=[0, 1, 0], createUVs=2, constructionHistory=1, name='Button1')
cmds.move(-1.8, 7.7, 0, 'Button1', relative=True)

cmds.duplicate(returnRootsOnly=True)
cmds.duplicate(returnRootsOnly=True)
cmds.move(0.25, -2, 0, 'Button2', relative=True)
cmds.move(-1, -3.8, 0, 'Button3', relative=True)

cmds.polyCube(width=.2, height=.2, depth=1, subdivisionsX=1, subdivisionsY=1, subdivisionsZ=1, axis=[0, 1, 0], createUVs=4, constructionHistory=1, name='Arm_L')
cmds.move(0, 8, 2, 'Arm_L', relative=True)
cmds.polyExtrudeFacet('Arm_L.f[0]', constructionHistory=1, keepFacesTogether=1, pivotX=0, pivotY=8, pivotZ=2.5, divisions=1, twist=1, taper=1, off=0, thickness=0, smoothingAngle=30)
cmds.setAttr('polyExtrudeFace1.localTranslate', 0, 0.5, 1.2, type='double3')

cmds.polyCube(width=.2, height=.2, depth=1, subdivisionsX=1, subdivisionsY=1, subdivisionsZ=1, axis=[0, 1, 0], createUVs=4, constructionHistory=1, name='Arm_R')
cmds.move(0, 8, -2, 'Arm_R', relative=True)
cmds.polyExtrudeFacet('Arm_R.f[2]', constructionHistory=1, keepFacesTogether=1, pivotX=0, pivotY=8, pivotZ=-2.5, divisions=1, twist=1, taper=1, off=0, thickness=0, smoothingAngle=30)
cmds.setAttr('polyExtrudeFace2.localTranslate', 0, 0.2, 1.2, type='double3')

cmds.polySoftEdge('Bottom', angle=180, constructionHistory=1)
cmds.polySoftEdge('Middle', angle=180, constructionHistory=1)
cmds.polySoftEdge('Top', angle=180, constructionHistory=1)
cmds.polySoftEdge('Eye_L', angle=180, constructionHistory=1)
cmds.polySoftEdge('Eye_R', angle=180, constructionHistory=1)
cmds.polySoftEdge('Button1', angle=180, constructionHistory=1)
cmds.polySoftEdge('Button2', angle=180, constructionHistory=1)
cmds.polySoftEdge('Button3', angle=180, constructionHistory=1)
cmds.select(clear=True)