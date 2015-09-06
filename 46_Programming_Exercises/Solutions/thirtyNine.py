# -*- coding: utf-8 -*-
# Problem Statement
# Write a program able to play the "Guess the number"-game, where the
# number to be guessed is randomly chosen between 1 and 20. This is
# how it should work when run in a terminal:
#
# >>> import guess_number
# Hello! What is your name?
# Torbjörn
# Well, Torbjörn, I am thinking of a number between 1 and 20.
# Take a guess.
# 10
# Your guess is too low.
# Take a guess.
# 15
# Your guess is too low.
# Take a guess.
# 18
# Good job, Torbjörn! You guessed my number in 3 guesses!

__author__ = "Asiful Nobel"

import random

def guess_number():
    print "Hello! What is your name?"

    try:
        userName = raw_input()
    except EOFError:
        return

    print "Well, " + userName + ", I am thinking of a number between 1 and 20."
    actualNumber = random.choice(range(1,20))
    guesses = 0
    guessedNumber = 0

    while(guessedNumber != actualNumber):
        print "Take a guess."
        try:
            guessedNumber = input()
        except (EOFError, SyntaxError):
            print "No input was received."
            return
        guesses += 1

        if guessedNumber > actualNumber:
            print "Your guess is too high."
        elif guessedNumber < actualNumber:
            print "Your guess is too low."
        else:
            print "Good job, " + userName + "! You guessed my number in " + str(guesses) + " guesses"


guess_number()
