import maya.cmds as cmds


def sequential_rename(name_format):
    selection = cmds.ls(sl=True)
    polygons = cmds.filterExpand(selection, sm=12)
    arg_length = len(name_format)
    tokens = name_format.split('#')
    print tokens
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
