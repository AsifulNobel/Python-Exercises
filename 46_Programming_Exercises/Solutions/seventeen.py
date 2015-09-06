# Problem Statement
# Write a version of a palindrome recognizer that also accepts phrase palindromes
# such as "Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on
# no pets", "Sit on a potato pan, Otis", "Lisa Bonet ate no basil", "Satan, oscillate
# my metallic sonatas", "I roamed under it as a tired nude Maori", "Rise to vote sir",
# or the exclamation "Dammit, I'm mad!". Note that punctuation, capitalization and spacing
# are usually ignored.

__author__ = "Asiful Nobel"

import re

def palindrome_recognizer(input_string):
    plain_string = "".join(re.findall(r"[a-zA-Z]", input_string)).lower()

    if plain_string.isalnum():
        if plain_string[0:len(plain_string)/2] == plain_string[-1:-(len(plain_string)/2)-1:-1]:
            return True
    return False


def main():
    print "Is the phrase palindrome? %s" %palindrome_recognizer(raw_input("Enter phrase to check palindromeness: "))

if __name__ == "__main__":
    main()
