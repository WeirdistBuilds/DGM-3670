import maya.cmds as cmds
import random


def random_spawn(amount, grow_flag, move_range, scale_lower, scale_upper):
    spawn_num = 1
    selection = cmds.ls(sl=True)
    polygons = cmds.filterExpand(selection, sm=12)
    if len(polygons) > 1:
        poly = cmds.polyUnite(polygons)
    else:
        poly = polygons
    cmds.rename(poly[0], 'Spawn_' + str(spawn_num))
    polygons[0] = 'Spawn_' + str(spawn_num)
    cmds.DeleteHistory((polygons[0]))
    cmds.xform('Spawn_' + str(spawn_num), pivots=(0, 0, 0), ws=True)
    if grow_flag:
        i = 0
        while i < amount:
            polygon = cmds.duplicate('Spawn_' + str(spawn_num))
            cmds.rename(polygon[0], 'CurrentSpawn')
            current_position = cmds.xform('CurrentSpawn', ws=True, query=True, translation=True)
            move_adj_x = random.randrange(-1 * move_range, move_range)
            move_adj_z = random.randrange(-1 * move_range, move_range)
            x = current_position[0] + move_adj_x
            y = current_position[1]
            z = current_position[2] + move_adj_z
            scale_adj = random.randrange(scale_lower, scale_upper)
            cmds.scale(scale_adj, scale_adj, scale_adj, 'CurrentSpawn')
            cmds.move(x, y, z, 'CurrentSpawn')
            spawn_num += 1
            cmds.rename('CurrentSpawn', 'Spawn_' + str(spawn_num))
            polygons[len(polygons) - 1] = 'Spawn_' + str(spawn_num)
            i += 1
    else:
        i = 0
        while i < amount:
            polygon = cmds.duplicate('Spawn_' + str(spawn_num))
            cmds.rename(polygon[0], 'CurrentSpawn')
            x = random.randrange(-1 * move_range, move_range)
            z = random.randrange(-1 * move_range, move_range)
            scale_adj = random.randrange(scale_lower, scale_upper)
            cmds.scale(scale_adj, scale_adj, scale_adj, 'CurrentSpawn')
            cmds.move(x, 0, z, 'CurrentSpawn', ws=True)
            spawn_num += 1
            cmds.rename('CurrentSpawn', 'Spawn_' + str(spawn_num))
            polygons[len(polygons) - 1] = 'Spawn_' + str(spawn_num)
            i += 1

    cmds.group(polygons, name='Geometry')


random_spawn(200, True, 10, 1, 2)