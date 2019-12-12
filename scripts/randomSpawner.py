import maya.cmds as cmds
import random


def random_spawner(amount, grow_flag, move_range, scale_lower, scale_upper):
    spawn_num = 1
    duplicates = list()
    selection = cmds.ls(sl=True)
    polygons = cmds.filterExpand(selection, sm=12)
    if len(polygons) > 1:
        poly = cmds.polyUnite(polygons)
    else:
        poly = polygons
    cmds.rename(poly[0], 'Spawn_' + str(spawn_num))
    duplicates.append('Spawn_' + str(spawn_num))
    polygons[0] = 'Spawn_' + str(spawn_num)
    cmds.DeleteHistory((polygons[0]))
    cmds.xform('Spawn_' + str(spawn_num), pivots=(0, 0, 0), ws=True)
    if grow_flag:
        i = 0
        while i < amount:
            polygon = cmds.duplicate('Spawn_' + str(spawn_num))
            cmds.rename(polygon[0], 'CurrentSpawn')
            current_position = cmds.xform('CurrentSpawn', ws=True, query=True, translation=True)
            move_adj_x = (random.randrange(-1000 * move_range, 1000 * move_range)) / 1000
            move_adj_z = (random.randrange(-1000 * move_range, 1000 * move_range)) / 1000
            x = current_position[0] + move_adj_x
            y = current_position[1]
            z = current_position[2] + move_adj_z
            scale_adj = (random.randrange(1000 * scale_lower, 1000 * scale_upper)) / 1000
            cmds.scale(scale_adj, scale_adj, scale_adj, 'CurrentSpawn')
            cmds.move(x, y, z, 'CurrentSpawn')
            spawn_num += 1
            cmds.rename('CurrentSpawn', 'Spawn_' + str(spawn_num))
            duplicates.append('Spawn_' + str(spawn_num))
            i += 1
    else:
        i = 0
        while i < amount:
            polygon = cmds.duplicate('Spawn_' + str(spawn_num))
            cmds.rename(polygon[0], 'CurrentSpawn')
            x = (random.randrange(-1000 * move_range, 1000 * move_range)) / 1000
            z = (random.randrange(-1000 * move_range, 1000 * move_range)) / 1000
            scale_adj = (random.randrange(1000 * scale_lower, 1000 * scale_upper)) / 1000
            cmds.scale(scale_adj, scale_adj, scale_adj, 'CurrentSpawn')
            cmds.move(x, 0, z, 'CurrentSpawn', ws=True)
            spawn_num += 1
            cmds.rename('CurrentSpawn', 'Spawn_' + str(spawn_num))
            duplicates.append('Spawn_' + str(spawn_num))
            i += 1
    cmds.group(duplicates, name='Geometry')
