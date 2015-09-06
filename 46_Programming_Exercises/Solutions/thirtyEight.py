# Problem Statement
# Write a program that will calculate the average word length of a text
# stored in a file (i.e the sum of a all the lengths of the word tokens in
# the text, divided by the number of word tokens)

__author__ = "Asiful Nobel"

from __future__ import division
import re

def averageWordLen():
    fileName = raw_input("Enter file name: ")

    with open(fileName, "rb") as wordFile:
        words = re.findall(r'\w+', wordFile.read())
        totalWordNumber = 0
        allWordLength = 0

        for word in words:
            totalWordNumber += 1
            allWordLength += len(word)
        print "\nAverage word length: " + "{:0.2f}".format(allWordLength/totalWordNumber) + " characters"

averageWordLen()
