def Add(values):
    '''
    Adds list of numbers and returns result
    input: list of float/int values
    return: float
    '''

    # sum = value1 + value2
    # return sum

    # return value1 + value2

    sum = 0
    for val in values:
        if type(val) == 'int' or type(val) == 'float':
            sum += val
        else:
            print "you're a dummy! You can't add " , val

    return sum


Add([1, 45, 2.6, 3, 53, 12.2])

help(Add)


def Power(value, power):
    import math
    return math.pow(value, power)