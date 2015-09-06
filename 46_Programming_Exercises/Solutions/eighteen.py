# Problem Statement
# A pangram is a sentence that contains all the letters of the English
# alphabet at least once, for example: the quick brown fox jumps over the
# lazy dog. Your task here is to write a function to check a sentence to
# see if it is a pangram or not.

__author__ = "Asiful Nobel"

import re

def pangram_check(inputString):
        abcdString = "abcdefghijklmnopqrstuvwxyz"            # Same thing can be achieve with string.lowercase()
        filteredString = ''.join(sorted(set(re.findall(r"[a-zA-Z]", inputString.lower()))))
                                                             # Extracted letters from the string and made those lowercase
                                                             # removed the duplicates and sorted those into a list
                                                             # then joined the list into a string
        if filteredString == abcdString:
            return True
        else:
            return False

print pangram_check(raw_input("Enter a sentence: "))
