# Problem Statement
# Define a procedure histogram() that takes a list of integers
# and prints a histogram to the screen. For example, histogram([4, 9, 7])
# should print the following:
# ****
# *********
# *******

__author__ = "Asiful Nobel"

def histogram(inputs):
    if type(inputs) is list:
        for values in inputs:
            print values * '*'
    else:
        print "List of integers is expected"

histogram(input("Enter a list of integers =>>> "))
