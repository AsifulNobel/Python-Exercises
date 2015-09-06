# Problem Statement
# "99 Bottles of Beer" is a traditional song in the United States and Canada.
# It is popular to sing on long trips, as it has a very repetitive format which
# is easy to memorize, and can take a long time to sing. The song's simple lyrics
# are as follows:
#     99 bottles of beer on the wall, 99 bottles of beer.
#     Take one down pass it around, 98 bottles of beer on the wall.
# The Same verse is repeated, each time with one fewer bottle. The song is completed
# when the singer or singers reach zero.
# Your task here is to write a Python program capable of generating all the verses of
# the song.

__author__ = "Asiful Nobel"

def song():
    count = 99
    while count > 0:
        if count == 1:
            print str(count) + " bottle of beer on the wall, " + str(count) + " bottle of beer on the wall."
            count -= 1
            print "Take one down pass it around, " + str(count) + " bottle of beer on the wall."
        else:
            print str(count) + " bottles of beer on the wall, " + str(count) + " bottles of beer on the wall."
            count -= 1
            print "Take one down pass it around, " + str(count) + " bottles of beer on the wall."

song()
