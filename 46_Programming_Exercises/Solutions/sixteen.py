# Problem Statement
# Write a function filter_long_words() that takes a list of words
# and an integer n and returns the list of words that are longer
# than n

__author__ = "Asiful Nobel"

def filter_long_words(inputs, n):
    longWords = []

    for word in inputs:
        if len(word) > n:
            longWords.append(word)

    return longWords


print filter_long_words(input("Enter a list of words >>> "), \
                        input("Enter length constraint integer >>> "))
