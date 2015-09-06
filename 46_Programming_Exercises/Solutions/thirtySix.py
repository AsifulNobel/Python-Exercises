# Problem Statement
# A hapax legomenon (often abbreviated to hapax) is a word which occurs
# only once in either the written record of a language, the works of an
# author, or in a single text. Define a function that given the file
# name of a text will return all its hapaxes. Make sure your program
# ignores capitalization.

__author__ = "Asiful Nobel"

import re, sys

def find_hapax_legomenons(filename = 'thirtySixInput.txt'):
    wordDictionary = {}
    hapax_legomenons = []

    # Get words in the file
    file = open( filename, 'r' )
    words = re.findall( '\w+', file.read() )

    for word in words:
        word = word.lower()

        if word in wordDictionary.keys():
            wordDictionary[word] += 1
        else:
            wordDictionary[word] = 1

    for word in wordDictionary:
        if wordDictionary[word] == 1:
            hapax_legomenons.append(word)

    print "\n\nHapax >>>> ", hapax_legomenons

if __name__ == "__main__":
    try:
        find_hapax_legomenons(sys.argv[1])
    except IndexError:
        find_hapax_legomenons()
