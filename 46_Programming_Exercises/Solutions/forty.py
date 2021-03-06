# Problem 40: An anagram is a type of word play, the result of rearranging the
# letters of a word or phrase to produce a new word or phrase, using all the
# original letters exactly once; e.g., orchestra = carthorse, A decimal point
# = I'm a dot in place. Write a Python program that, when started 1) randomly
# picks a word w from given list of words, 2) randomly permutes w (thus creating
# an anagram of w), 3) presents the anagram to the user, and 4) enters an
# interactive loop in which the user is invited to guess the original word. It
# may be a good idea to work with (say) colour words only. The interaction with
# the program may look like so:
#
# >>> import anagram
# Colour word anagram: onwbr
# Guess the colour word!
# black
# Guess the colour word!
# brown
# Correct!
#
# Note: The specification of this game is not entirely correct - a word anagram
# as described here is actually a permutation of the word, whereas strictly
# speaking an anagram must be another valid word (in the same language).
#
# This implementation ensures that the secret word presented to the player is
# indeed a word with an anagram (in the proper sense) and not just a
# permutation.  To make the game a bit more interesting the words are not
# restricted to colours but obtained from a list of 109592 English (lowercase)
# words generated from a local copy of a file located here:
#
#    http://www-01.sil.org/linguistics/wordlists/english/wordlist/wordsEn.txt
#
# subject to the constraint that the word contains at least 5 characters and at
# most 7 - the number of permutations of a word of length N is N! and exceeds
# 5040 for N > 7.
#
# Another addition is of a main loop for the user to keep playing new games,
# until they quit.

__author__ = "Sandeep Murthy"   # Modified by Asiful Nobel

def guess_the_anagram():

    from random import randint
    from itertools import permutations

    def build_word_list():
        file_path = 'fortyDictionary.txt'
        # This is needed only if the dictionary file consists of words with lengths less than 5 and more than 7
        # return [word.strip() for word in open( file_path, 'rb' ) \
        #         if not word.strip() == '' \
        #         and len(word.strip()) in range(5, 8)]
        return [word.strip() for word in open(file_path, 'rb')]

    def get_secret_word_with_anagram(words):
        while True:
            word = words[randint(0, len(words))]
            perms = permutations(word)
            for count, perm in enumerate(perms):
                perm_word = ''.join(list(perm))
                if perm_word in words and not perm_word == word:
                    return word, perm_word
            words.remove(word)

    def play_new_game(words):

        print '\nSearching the dictionary for a secret word with anagram ... '
        secret_word, anagram = get_secret_word_with_anagram(words)

        guess = ''

        while not guess == secret_word:
            print '\nGuess the secret word from this anagram: {}.'.\
                format( anagram )
            print '(Press x to exit at any stage).\n'
            guess = raw_input('Your guess: ')
            if not guess == '':
                if set(guess).issubset(set(secret_word)) and \
                    len(guess) == len(secret_word):
                    if guess == secret_word:
                        print 'Correct!'
                    else:
                        print 'Incorrect!'
                    continue
                else:
                    if not guess == 'x':
                        print 'Incorrect!  Your guess must contain only and all the letters from the original anagram {}.'.format(anagram)
                        continue
                    else:
                        print 'The secret word was {}.'.format(secret_word)
                        return 'exit'
            else:
                print 'Incorrect!  Your guess must contain only and all the letters from the original anagram {}.'.format(anagram)
                continue
            return 'correct guess'

    print '\nWelcome to the Guess the Anagram game!'
    print '\nYou must guess the anagram of a secret word (lowercase, English) generated by the computer, between 5 and 7 characters in length.'

    words = build_word_list()
    result = play_new_game(words)
    while not result == 'exit':
        if result == 'correct guess':
            option = raw_input( '\nDo you wish to play a new game (n) or exit (x)? ' )
            if option == 'n':
                result = play_new_game( words )
                continue
            elif option == 'x':
                result = 'exit'
                break
            else:
                continue
        else:
            break
    print 'Bye!'
