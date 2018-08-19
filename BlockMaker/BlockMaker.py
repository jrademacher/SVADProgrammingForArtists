import maya.cmds as cmds

CountX = 10
CountY = 20
CountZ = 30
for x in range(1, CountX):
    for y in range(1, CountY):
        for z in range(1, CountZ):
            newcube = cmds.polyCube()
            cmds.xform(newcube, t=[x, y, z])
# Example variation
'''
t = [x^z, y^2, z/y]
'''