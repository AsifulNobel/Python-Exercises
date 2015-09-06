# Problem Statement
# Write a function char_freq() that takes a string and builds a frequency
# listing of the characters contained in it. Represent the frequency listing
# as a Python dictionary. Try it with something like char_freq("abbabcbdbabdbdbdbabababcbcbab")
__author__ = "Asiful Nobel"

import collections

def char_freq(input_string):
    letterDict = collections.OrderedDict()
    for letter in sorted(set(input_string)):
        letterDict[letter] = 0
    for letter in input_string:
        letterDict[letter] += 1

    print "Character frequency listing of " + input_string + " is >>>"
    for key, value in letterDict.items():
        print "\t"*6 + str(key) + " : " + str(value)

char_freq(raw_input("Enter string: "))
