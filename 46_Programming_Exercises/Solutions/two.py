# Problem Statement
# Define a function max_of_three() that takes two numbers as arguments and returns the
# largest of them.
__author__ = "Asiful Nobel"

import sys

def max_of_three(x, y, z):
    try:                # Check to see if the arguments are numbers
        x = float(x)
        y = float(y)
        z = float(z)

        maxVal = x
        if y > maxVal:
            maxVal = y
        if z > maxVal:
            maxVal = z

        return maxVal
    except ValueError:
        return "numbers were expected as arguments"

if __name__ == "__main__":
    try:
        print max_of_three(sys.argv[1], sys.argv[2], sys.argv[3])     # takes arguments from command-line
    except IndexError:
        print "Not enought inputs"
