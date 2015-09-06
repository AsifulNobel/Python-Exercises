# Problem Statement
# According to Wikipedia, a semordnilap is a word or phrase that
# spells a different word or phrase backwards. ("Semordnilap" is
# itself "palindromes" spelled backwards.) Write a semordnilap
# recogniser that accepts a file name (pointing to a list of words)
# from the user and finds and prints all pairs of words that are
# semordnilaps to the screen. For example, if "stressed" and "desserts"
# is part of the word list, the the output should include the pair
# "stressed desserts". Note, by the way, that each pair by itself
# forms a palindrome!

__author__ = "Asiful Nobel"

def semordnilap_recogniser(fileName):
    with open(fileName, "rb") as semordnilapFile:
        lines = semordnilapFile.readlines()             # Read all lines from the file and store those as a list
        words = (' '.join(lines).lower()).split()       # Turn the lines elements into a continuous string by joining those
                                                        # then make those lowercase and again split those into a list
        for word in words:
            if word[::-1] in words:
                print word + " " + word[::-1]


semordnilap_recogniser(raw_input("Enter file name: "))
