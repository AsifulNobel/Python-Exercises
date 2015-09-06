# Problem Statement
# Write a function that takes a character (i.e. a
# string of length 1) and return True if it is a vowel,
# False otherwise

__author__ = "Asiful Nobel"

import sys

def vowelCheck(char):
    # The approach is to check if the input character is in vowels list
    # if the character is present in list, then True will be returned and vice versa

    vowels = ['a', 'e', 'i', 'o', 'u',\
                'A', 'E', 'I', 'O', 'U']
    if len(char) > 1:
        return "Single character was expected"
    elif type(char) is str:
        if char in vowels:
            return True
        else:
            return False
    else:
        return "Wrong Type of Input"

if __name__ == "__main__":
    try:
        print "Is %s a vowel? =>>> %s" %(sys.argv[1], vowelCheck(sys.argv[1]))
    except IndexError:                              # In case, no argument is passed from command-line
        print "One command-line argument was expected"
