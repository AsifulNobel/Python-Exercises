# Using the higher order function reduce(), write a function max_in_list()
# that takes a list of numbers and returns the largest one. Then ask yourself:
# why define and call a new function, when I can just as well call the reduce()
# function directly?
__author__ = "Asiful Nobel"

def max_in_list(inputList):
    maxValue = inputList[0]
    for value in inputList[1:]:
        if value > maxValue:
            maxValue = value
    return maxValue

# Found a python 2.x problem: Python cannot handle integer/decimal numbers with leading zeros
# because leading zero such as '0127' means that it is a octal number, while other things in the
# input list is probably with base 10. So, do not input with leading zero or invalid token
# syntax error will be raised
print "Largest in list: {0}".format(max_in_list(input("Enter list of numbers: ")))
print "Largest in list: {0}".format(reduce(lambda a, b: a if a>b else b, input("Enter list of numbers: ")))

# Calling reduce in a pythonic code decreases readability of the code
# reduce function has been remove from python 3.x as built-in to functools
