# Problem Statement
# Define a function reverse() that computes the
# reversal of a string. For example, reverse("I am
# testing") should return the string "gnitset ma I"

__author__ = "Asiful Nobel"

def reverse(inputs):
    output = inputs[::-1]    # Iterates through the list from the last index to first index
                            # and returns a list
    return output

print reverse(raw_input("Enter string: "))
