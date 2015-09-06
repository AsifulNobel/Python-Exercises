# Using the higher order function filter(), define a function filter_long_words()
# that takes a list of words and an integer n and returns the list of words that
# are longer than n.
__author__ = "Asiful Nobel"

def filter_long_words(wordList, n):
    return filter(lambda word: len(word) > n, wordList)

words = input("Enter list of words: ")
maxLength = input("Enter maximum length of words: ")
print "List of words with length more than {0}: {1}".format(maxLength, filter_long_words(words, maxLength))
