# Write a program that maps a list of words into a list of integers representing
# the lengths of the correponding words. Write it in three different ways:
# 1) using a for-loop, 2) using the higher order function map(), and 3) using list comprehensions.
__author__ = "Asiful Nobel"

def mapWordLength(words):
    lengthList = []
    for word in words:
        lengthList.append(len(word))
    return lengthList

wordList = input("Enter list of words: ")

print "Using for-loop: {0}".format(mapWordLength(wordList))
print "Using map() function: {0}".format(map(lambda word: len(word), wordList))
print "Using list comprehension: {0}".format([len(word) for word in wordList])
