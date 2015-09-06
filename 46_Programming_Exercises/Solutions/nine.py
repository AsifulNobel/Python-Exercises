# Problem Statement
# Define a function is_member() that takes a value
# (i.e. a number, string etc) x and a list of values
# a, and returns True if x is a memeber of a, False
# otherwise. (Note that this is exactly what the in
# operator does, but for the sake of the exercise you
# should pretend Python did not have this operator.)

__author__ = "Asiful Nobel"

def is_member(x, a):
    try:
        for values in a:
            if x == values:
                return True
        return False
    except TypeError:
        return "Wrong Type of Arguments"

print is_member(input("Enter the number you want to search: "), \
                input("Enter the list you want to search for the number: "))
