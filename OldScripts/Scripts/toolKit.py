import maya.cmds as cmds
import random


class ToolKit:
    def __init__(self):
        pass

    class Calculator:
        def __init__(self):
            pass

        @staticmethod
        def value_check(values):
            """
            Checks values to ensure all values are of type float or int
            input: list
            return: list of only int or float values
            """
            result = list()
            for val in values:
                if type(val) == int or type(val) == float:
                    result.append(val)
            return result

        def add(self, values):
            """
            Adds list of numbers and returns result
            input: list of float/int values
            return: float
            """
            result = 0
            current = self.value_check(values)
            for val in current:
                result += val
            print(str(values) + ' adds up to ' + str(result))
            return result

        def subtract(self, values):
            """
            Subtracts a list of numbers from the first number in the list and returns result
            input: list of float/int values
            return: float
            """

            current = self.value_check(values)
            result = current[0]
            for val in values[1:]:
                result -= val
            print(str(values[0]) + ' minus ' + str(values[1:]) + ' is ' + str(result))
            return result

        def multiply(self, values):
            """
            Multiplies a list of numbers and returns result
            input: list of float/int values
            return: float
            """
            current = self.value_check(values)
            result = current[0]
            for val in current:
                result *= val
            print(str(values) + ' multiplies up to ' + str(result))
            return result

        def divide(self, values):
            """
            Subtracts a list of numbers from the first number in the list and returns result
            input: list of float/int values
            return: float
            """

            current = self.value_check(values)
            result = current[0]
            for val in values[1:]:
                if val != 0:
                    result /= val
                else:
                    print('Error: Divide by zero')
            print(str(values[0]) + ' divided by ' + str(values[1:]) + ' is ' + str(result))
            return result

        def power(self, values):
            """
            Raises the value of 'values[0]' to the power of 'values[1]'
            input: list of float/int values
            return: float
            """
            import math
            current = self.value_check(values)
            if len(current) >= 2:
                result = math.pow(current[0], current[1])
                print(str(current[0]) + ' to the power of ' + str(current[1]) + ' is ' + str(result))
                return result
            else:
                print('Error: Not enough valid float/int values in list')
                return 0

        def mean(self, values):
            """
            Finds the mean of a list of values
            input: list of float/int values
            return: float
            """
            current = self.value_check(values)
            result = self.add(current) / len(current)
            print('The mean of ' + str(values) + ' is ' + str(result))
            return result

        def median(self, values):
            """
            Finds the median of a list of values
            input: list of float/int values
            return: float
            """
            import math
            current = self.value_check(values)
            current.sort()
            middle = int(math.floor(len(current) / 2))
            if len(current) % 2 == 0:
                result = (current[middle - 1] + current[middle]) / 2
            else:
                result = current[middle]
            print('The median of ' + str(current) + ' is ' + str(result))
            return result

        def mode(self, values):
            """
            Finds the mode of a list of values
            input: list of float/int values
            return: float
            """
            current = self.value_check(values)
            count = 1
            mode_count = 1
            current.sort()
            number = current[0]
            result = number

            for val in current[1:]:
                if val == number:
                    count += 1
                else:
                    if count > mode_count:
                        mode_count = count
                        result = number
                    count = 1
                    number = val
            if mode_count == 1:
                print('All numbers in this list appear only once')
                return 0
            else:
                print('The mode is ' + str(result) + ' which appears ' + str(mode_count) + ' times')
                assert isinstance(result, object)
                return result


def center_locator(give_individual_centers):
    """
    Finds the median of a list of values
    input: boolean
    return: none
    """
    sels = cmds.ls(sl=True)
    locators = list()
    min_x = list()
    min_y = list()
    min_z = list()
    max_x = list()
    max_y = list()
    max_z = list()
    total = [0, 0, 0]
    if give_individual_centers:
        for obj in sels:
            split_name = obj.split('.[]_:')
            new_name = ''
            for word in split_name:
                new_name += '%s_' % word
            new_name += 'Loc'
            bounding_box = cmds.xform(obj, query=True, ws=True, boundingBox=True)
            if obj(type='joint'):
                joint_translate = cmds.xform(obj, query=True, translation=True, worldSpace=True)
                joint_rotate = cmds.xform(obj, query=True, rotation=True, worldSpace=True)
                cmds.spaceLocator(name=new_name)
                cmds.xform(new_name, translation=joint_translate, worldSpace=True)
                cmds.xform(new_name, rotation=joint_rotate, worldSpace=True)
            else:
                x = (bounding_box[0] + bounding_box[3]) / 2
                y = (bounding_box[1] + bounding_box[4]) / 2
                z = (bounding_box[2] + bounding_box[5]) / 2
                cmds.spaceLocator(name=new_name)
                cmds.xform(new_name, worldSpace=True, translation=(x, y, z))
                current_rotation = cmds.xform(obj, worldSpace=True, rotation=True, query=True)
                rot_x = current_rotation[0]
                rot_y = current_rotation[1]
                rot_z = current_rotation[2]
                cmds.xform(new_name, worldSpace=True, rotation=(rot_x, rot_y, rot_z))
            locators.append(new_name)
        return locators
    else:
        for obj in sels:
            bounding_box = cmds.xform(obj, query=True, worldSpace=True, boundingBox=True)
            min_x.append(bounding_box[0])
            min_y.append(bounding_box[1])
            min_z.append(bounding_box[2])
            max_x.append(bounding_box[3])
            max_y.append(bounding_box[4])
            max_z.append(bounding_box[5])
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
        cmds.xform('TrueCenter_Loc', worldSpace=True, translation=(total[0], total[1], total[2]))


def color_changer(color):
    """
    Changes color of object to specified color
    input: string (yellow, red, blue, green, purple, orange, black, or white)
    return: none
    """
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


def random_spawner(amount, grow_flag, move_range, scale_lower, scale_upper):
    """
    Randomly places duplicates of selected object around object
    input: int, boolean, float, float, float
    return: none
    """
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


def sequential_renamer(name_format):
    """
    Renames selected objects in sequential order
    input: string, with # signs in place of desired numbers
    return: none
    """
    selection = cmds.ls(sl=True)
    polygons = cmds.filterExpand(selection, sm=12)
    arg_length = len(name_format)
    tokens = name_format.split('#')
    print(tokens)
    tokens_length = len(tokens[0]) + len(tokens[len(tokens) - 1])
    num_length = arg_length - tokens_length

    i = 0
    while i < len(polygons):
        zero_string = ''
        loop_number = i + 1
        current_zeros = num_length - len(str(loop_number))
        j = 0
        while j < current_zeros:
            zero_string += '0'
            j += 1
        current_number = zero_string + str(loop_number)
        current_name = tokens[0] + current_number + tokens[len(tokens) - 1]
        cmds.rename(polygons[i], current_name)
        i += 1


def control_maker(color):
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
