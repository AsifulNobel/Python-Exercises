# Problem Statement
# Write a procedure char_freq_table() that, when run in a terminal,
# accepts a file name from the user, builds a frequency listing of
# the characters contained in the file, and prints a sorted and
# nicely formatted character frequency table to the screen.

__author__ = "Asiful Nobel"

from __future__ import division
import sys

def char_freq_table(fileName):
    lowerCaseAlphabets = "abcdefghijklmnopqrstuvwxyz"

    characterFreq = {}
    for character in lowerCaseAlphabets:
        characterFreq[character] = 0

    with open(fileName, "rb") as characterFile:
        lines = characterFile.read().lower()

        for character in lowerCaseAlphabets:
            characterFreq[character] += lines.count(character)

    totalCharacterCounts = 0
    for value in characterFreq.values():
        totalCharacterCounts += value

    print "\nCharacter Frequency Table"
    print "="*72
    print "Character " + " - "*5 + " Count " + " - "*5 + " Occurrence Percentage(%)"
    print "="*72
    for character, value in characterFreq.items():
        print " "*3 + character + " "*6 + " - "*5 + " " + ("{0:05d}".format(value)) \
        + " " + " - "*5 + " "*7 + ("{0:0.3f}".format((value/totalCharacterCounts)*100))


if __name__ == "__main__":
    char_freq_table(sys.argv[1])        # Use thirtyFourInput.txt as input
