# Problem Statement
# Define a function that computes the length of a
# given list or string. (It is true that Python has
# the len() function build in, but writing it yourself
# is nevertheless a good exercise)

__author__ = "Asiful Nobel"

import sys, ast

def lengthOfStr(inputs):
    length = 0

    try:
        cleanInput = ast.literal_eval(inputs)    # tries to turn list back to list from string type
                                                # If unsuccessful, then ValueError is raised
                                                # Then we can be sure that it is of str type
        for element in cleanInput:
            length += 1
    except (ValueError, TypeError):             # TypeError is raised in case of uniterable object like 'None'
        for element in inputs:
            length += 1

    return length

if __name__ == "__main__":
    try:
        print "Length of %s is %s" % (sys.argv[1], lengthOfStr(sys.argv[1]))
    except IndexError:                          # In case, no argument is passed from command-line
        print "Wrong number of Input"
        print "Usage: python three.py 'string'"
