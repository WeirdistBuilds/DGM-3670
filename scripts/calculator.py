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
            return result
