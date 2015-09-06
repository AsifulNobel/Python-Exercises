# -*- coding: utf-8 -*-
# Represent a small bilingual lexicon as a Python dictionary in the following fashion
# {"merry":"god", "christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":
# "år"} and use it to translate your Christmas cards from English into Swedish. Use
# the higher order function map() to write a function translate() that takes a list of
# English words and returns a list of Swedish words.

__author__ = "Asiful Nobel"

def translateEnglish(words):
    EtoSdictionary = {"merry": "god", "christmas": "jul", "and": "och", "happy": "gott",\
                     "new": "nytt", "year": "år"}
    return map(lambda word: EtoSdictionary[word], words)

# Use input e.g. ["merry", "new"]
inputList = input("Enter list of English Words: ")
translatedList = translateEnglish(inputList)

print "Translated Swedish Words: [",
for value in translatedList[:-1]:       # Printing list values like this instead of printing the list at once
    print value + ',',                  # helps to print the actual unicode characters
else:
    print translatedList[-1],
    print "]"
