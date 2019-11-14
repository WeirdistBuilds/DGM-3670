def valuecheck(values):
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


def add(values):
    """
    Adds list of numbers and returns result
    input: list of float/int values
    return: float
    """
    result = 0
    current = valuecheck(values)
    for val in current:
        result += val
    return result


def subtract(values):
    """
    Subtracts a list of numbers from the first number in the list and returns result
    input: list of float/int values
    return: float
    """

    current = valuecheck(values)
    result = current[0]
    for val in values[1:]:
        result -= val

    return result


def multiply(values):
    """
    Multiplies a list of numbers and returns result
    input: list of float/int values
    return: float
    """
    current = valuecheck(values)
    result = current[0]
    for val in current:
        result *= val
    return result


def divide(values):
    """
    Subtracts a list of numbers from the first number in the list and returns result
    input: list of float/int values
    return: float
    """

    current = valuecheck(values)
    result = current[0]
    for val in values[1:]:
        if val != 0:
            result /= val
        else:
            print 'Error: Divide by zero'

    return result


def power(values):
    """
    Raises the value of 'values[0]' to the power of 'values[1]'
    input: list of float/int values
    return: float
    """
    import math
    result = valuecheck(values)
    if len(result) >= 2:
        return math.pow(result[0], result[1])
    else:
        print 'Error: Not enough valid float/int values in list'


def mean(values):
    """
    Finds the mean of a list of values
    input: list of float/int values
    return: float
    """
    current = valuecheck(values)
    return add(current) / len(current)


def median(values):
    """
    Finds the median of a list of values
    input: list of float/int values
    return: float
    """
    import math
    current = valuecheck(values)
    current.sort()
    middle = int(math.floor(len(current) / 2))
    if len(current) % 2 == 0:
        return (current[middle - 1] + current[middle]) / 2
    else:
        return current[middle]


def mode(values):
    """
    Finds the mode of a list of values
    input: list of float/int values
    return: float
    """
    current = valuecheck(values)
    count = 1
    modecount = 1
    current.sort()
    number = current[0]
    result = number

    for val in current[1:]:
        if val == number:
            count += 1
        else:
            if count > modecount:
                modecount = count
                result = number
            count = 1
            number = val
    return "The mode is " + str(result) + " which appears " + str(modecount) + " times."