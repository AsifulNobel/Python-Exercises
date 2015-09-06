# Problem Statement
# Write a version of a palindrome recogniser that accepts a file name
# from the user, reads each line, and prints the line to the screen if
# it is a palindrome.

# Found out that if a normal script with no __name__ == "__main__" is imported,
# Then first that script runs and after that the script that imported the module
# will run
__author__ = "Asiful Nobel"

from seventeen import palindrome_recognizer

# Input the exact file name e.g. thirtyTwoInput.txt
fileName = raw_input("Enter file name that you want to check for palindromes: ")

try:
    with open(fileName, "rb") as palindromeFile:
        palindromeFile.seek(0)
        for line in palindromeFile.readlines():
            if palindrome_recognizer(line):
                print line
except IOError:
    print "No such file or directory"
