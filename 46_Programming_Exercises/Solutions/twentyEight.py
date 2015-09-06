# Write a function find_longest_word() that takes a list of words and
# returns the length of the longest one. Use only higher order functions.
__author__ = "Asiful Nobel"

def find_longest_word(wordList):
    # map function generates a list of wordlengths and passes it to reduce function
    # then reduce uses it to find the greatest number in the list using lambda expression

    return reduce(lambda x,y: x if x>y else y, map(lambda word: len(word), wordList))

print "Length of the longest word is {0}".format(find_longest_word(input("Enter list of words: ")))
