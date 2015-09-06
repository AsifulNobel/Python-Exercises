# Problem Statement
# Write a function translate() that will translate a text into "rovarspraket"
# (Swedish for "robber's language"). That is, double every consonant and place
# an occurrence of "o" in between. For example, translate("this is fun") should
# return the string "tothohisos isos fofunon".

__author__ = "Asiful Nobel"

import string, sys

def translate(sentence):
    vowels = 'aeiou'
    allChars = "".join(list(set(string.lowercase) - set(vowels)))

    for char in allChars:
        if char in sentence:
            replacedLetters = (char + 'o' + char)
            sentence = sentence.replace(char, replacedLetters)
    return sentence

if __name__ == '__main__':
    try:
        print translate(sys.argv[1].lower())
    except IndexError:
        print "Invalid input"
