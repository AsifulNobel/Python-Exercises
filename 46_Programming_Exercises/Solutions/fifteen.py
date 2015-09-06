# Problem Statement
# Write a function find_longest_word() that takes a list of words
# and returns the length of the longest one.
__author__ = "Asiful Nobel"

def find_longest_word(inputs):
    maxLen = len(inputs[0])
    for word in inputs[1:]:
        if len(word) > maxLen:
            maxLen = len(word)
    return maxLen

print find_longest_word(input("Enter a list of words >>> "))
