import maya.cmds as cmds


def center_locator(give_individual_centers, match_rotate):
    selection = cmds.ls(sl=True)
    current_position = [0, 0, 0]
    locators = list()
    min_x = list()
    min_y = list()
    min_z = list()
    max_x = list()
    max_y = list()
    max_z = list()
    total = [0, 0, 0]
    if give_individual_centers:
        i = 0
        while i < len(selection):
            current_name = selection[i]
            current_name_pieces = current_name.split('.[]_:')
            new_name = ''
            j = 0
            while j < len(current_name_pieces):
                new_name += current_name_pieces[j] + '_'
                j += 1
            current_name = new_name + '_Loc'
            bounding_box = cmds.xform(selection[i], query=True, ws=True, boundingBox=True)
            current_position[0] = (bounding_box[0] + bounding_box[3]) / 2
            current_position[1] = (bounding_box[1] + bounding_box[4]) / 2
            current_position[2] = (bounding_box[2] + bounding_box[5]) / 2
            cmds.spaceLocator(name=current_name)
            cmds.xform(current_name, t=(current_position[0], current_position[1], current_position[2]))
            if match_rotate:
                current_rotation = cmds.xform(selection[i], ro=True, q=True)
                cmds.xform(current_name, current_rotation[0], current_rotation[1], current_rotation[2], ro=True)
            locators.append(current_name)
            i += 1
    else:
        i = 0
        while i < len(selection):
            bounding_box = cmds.xform(selection[i], query=True, ws=True, boundingBox=True)
            min_x.append(bounding_box[0])
            min_y.append(bounding_box[1])
            min_z.append(bounding_box[2])
            max_x.append(bounding_box[3])
            max_y.append(bounding_box[4])
            max_z.append(bounding_box[5])
            i += 1
        min_x.sort()
        min_y.sort()
        min_z.sort()
        max_x.sort()
        max_y.sort()
        max_z.sort()
        total[0] = (min_x[0] + max_x[len(max_x) - 1]) / 2
        total[1] = (min_y[0] + max_y[len(max_y) - 1]) / 2
        total[2] = (min_z[0] + max_z[len(max_z) - 1]) / 2
        cmds.spaceLocator(name='TrueCenter_Loc')
        cmds.xform('TrueCenter_Loc', t=(total[0], total[1], total[2]))


center_locator(False, False)
