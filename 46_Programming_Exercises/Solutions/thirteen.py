# Problem Statement
# The function max() from exercise 1) and the function max_of_three
# from exercise 2) will only work for two and three numbers, respectively.
# But suppose we have a much larger number of numbers, or suppose we cannot
# tell in advance how many they are? Write a function max_in_list() that
# takes a list of numbers and returns the largest one.

__author__ = "Asiful Nobel"

def max_in_list(inputs):
    if type(inputs) is list:
        maxValue = inputs[0]
        for value in inputs[1:]:
            if value > maxValue:
                maxValue = value
        return maxValue
    else:
        return "List was expected as input"

try:
    print max_in_list(input("Enter a list >>> "))
except (EOFError, SyntaxError):
    pass
