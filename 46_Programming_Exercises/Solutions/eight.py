# Problem Statement
# Define a function is_palindrome() that recognizes palindromes
# (i.e. words that look the same written backwards). For example,
# is_palindrome("radar") should return True

__author__ = "Asiful Nobel"

def is_palindrome(input_String):
    if input_String == input_String[::-1]:
        return True
    else:
        return False

try:
    print "Enter Ctrl+D or Ctrl+Z to exit"
    while True:
        print is_palindrome(raw_input("Enter String: ").lower())
except EOFError:
    print
