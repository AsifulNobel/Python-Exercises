# Problem Statement
# The International Civil Aviation Organization (ICAO) alphabet assigns
# code words to the letters of the English alphabet acrophonically (Alfa
# for A, Bravo for B, etc.) so that critical combinations of letters (and
# numbers) can be pronounced and understood by those who transmit and
# receive voice messages by radio or telephone regardless of their native
# language, especially when the safety of navigation or persons is essential.
# Here is a Python dictionary covering one version of the ICAO alphabet:
#
# d = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo', 'f':'foxtrot',
#      'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett', 'k':'kilo', 'l':'lima',
#      'm':'mike', 'n':'november', 'o':'oscar', 'p':'papa', 'q':'quebec', 'r':'romeo',
#      's':'sierra', 't':'tango', 'u':'uniform', 'v':'victor', 'w':'whiskey',
#      'x':'x-ray', 'y':'yankee', 'z':'zulu'}
# Your task in this exercise is to write a procedure speak_ICAO() able to
# translate any text (i.e. any string) into spoken ICAO words. You need to
# import at least two libraries: os and time. On a mac, you have access to
# the system TTS (Text-To-Speech) as follows: os.system('say ' + msg), where
# msg is the string to be spoken. (Under UNIX/Linux and Windows, something
# similar might exist.) Apart from the text to be spoken, your procedure also
# needs to accept two additional parameters: a float indicating the length of
# the pause between each spoken ICAO word, and a float indicating the length of
# the pause between each word spoken.

__author__ = "Asiful Nobel"

import pyttsx, time, sys, ast

def speak_ICAO(inputString=["help"], letterPause=0.2, wordPause=0.7):
    icaoDict = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo', 'f':'foxtrot',
         'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett', 'k':'kilo', 'l':'lima',
         'm':'mike', 'n':'november', 'o':'oscar', 'p':'papa', 'q':'quebec', 'r':'romeo',
         's':'sierra', 't':'tango', 'u':'uniform', 'v':'victor', 'w':'whiskey',
         'x':'x-ray', 'y':'yankee', 'z':'zulu'}

    engine = pyttsx.init()              # Initialized the Text-To-Speech module class
    rate = engine.getProperty('rate')   # Returns the talking speed of the bot
    engine.setProperty('rate', 180)     # Decreased talking speed slightly(Default: 200)

    print "\n" + str(inputString)
    for index, word in enumerate(inputString, start=1):
        for character in word:
            if character in icaoDict.keys():
                engine.say(icaoDict[character])
                engine.runAndWait()     # Engine waits for calling
                time.sleep(letterPause) # Makes the current thread sleep, simulating a pause between ICAO words
            elif character.isdigit():
                engine.say(character)
                engine.runAndWait()

        if index < len(inputString):
            time.sleep(wordPause)       # Makes the current thread sleep, simulating a pause between input words


if __name__ == "__main__":
    # Input example: python thirtyFive.py "Help" 0.2 0.7
    try:
        speak_ICAO(sys.argv[1].lower().split(), ast.literal_eval(sys.argv[2]), ast.literal_eval(sys.argv[3]))
    except IndexError:
        speak_ICAO()
