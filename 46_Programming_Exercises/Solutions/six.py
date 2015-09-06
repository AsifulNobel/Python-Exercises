# Problem Statement
# Define a function sum() and a function multiply()
# that sums and multiplies (respectively) all the numbers
# a list of numbers. For example, sum([1, 2, 3, 4]) should
# return 10, and multiply([1, 2, 3, 4]) should return 24

__author__ = "Asiful Nobel"

def sum(elements):
    result = 0
    for element in elements:
        result += element
    return result

def multiply(elements):
    result = 1
    for element in elements:
        result *= element
    return result

print sum(input("Sum of: "))
print multiply(input("Product of:"))
