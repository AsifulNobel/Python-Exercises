# Problem Statement
# Define a function generate_n_chars() that takes an integer
# n and a character c and returns a string, n characters long,
# consisting only of c:s. For example, generate_n_chars(5, "x")
# should return the string 'xxxxx'. (Python is unusual in that you
# can actually write an 5*'x' that will evaluate to 'xxxxx'. For the
# sake of the exercise you should ignore that the problem can be solved
# in this manner)

__author__ = "Asiful Nobel"

def generate_n_chars(n, char):
    word = ""
    if len(char) == 1:
        for count in xrange(0, n):
            word += char
        return word
    else:
        return "Too many input characters. Only one needed."


print generate_n_chars(input("N: "), raw_input("Character: "))
