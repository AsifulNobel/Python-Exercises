# Problem Statement
# Write a program that maps a list of words into a list of
# integers representing the lengths the of the corresponding words

__author__ = "Asiful Nobel"

def lengthList(listNum, listWord):
    newList = []
    for value in listNum:
        for word in listWord:
            if len(word) == value:
                newList.append(word)
    return newList

listNum = input("Enter list of lengths of words: ")
listWord = input("Enter list of words: ")
print lengthList(listNum, listWord)
