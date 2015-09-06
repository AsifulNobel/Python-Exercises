# Problem Statement
# Define a function max() that takes two numbers as arguments and returns the
# largest of them. Use the if-then-else construct available in Python.

__author__ = "Asiful Nobel"

import sys

def max(x, y):
    try:                # Check to see if the arguments are numbers
        x = float(x)
        y = float(y)

        maxVal = x
        if y > maxVal:
            maxVal = y

        return maxVal
    except ValueError:
        return "numbers were expected as arguments"

if __name__ == "__main__":
    try:
        print max(sys.argv[1], sys.argv[2])     # takes arguments from command-line
    except IndexError:                          # In case, no argument is passed from command-line
        print "Not enought inputs"              # (del max) command to get-back the built-in max method globally
