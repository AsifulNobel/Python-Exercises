# Problem Statement
# Represent a small bilingual lexicon as a Python dictionary in the following fashion
# {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":
# "ar"} and use it to translate your Christmas cards from English into Swedish. That is,
# write a function translate() that takes a list of English words returns a list of Swedish
# words.
__author__ = "Asiful Nobel"


def translateEnglish(words):
    EtoSdictionary = {"merry": "god", "christmas": "jul", "and": "och", "happy": "gott",\
                     "new": "nytt", "year": "ar"}
    translatedWords = []
    for word in words:
        if word in EtoSdictionary:
            translatedWords.append(EtoSdictionary[word])
    return translatedWords

# Use input e.g. ["merry", "nytt"]
print "Translated Swedish Words >>> %s" %translateEnglish(input("Enter list of English Words: "))
