# Problem Statement
# Write a program that given a text file will create a new text
# file in which all the lines from the original file are numbered
# from 1 to n (where n is the number of lines in the file).

__author__ = "Asiful Nobel"

def lineNumberAdd():
    fileName = raw_input("Enter name of the file: ")
    oldFile = open(fileName, "rb")
    newFile = open(("new_" + fileName), "wb")

    width = 0
    for content in oldFile:
        width += 1

    width = len(str(width))
    oldFile.seek(0)

    for lineNum, content in enumerate(oldFile, start=1):
        newFile.write("{:{width}}  {}".format(lineNum, content, width=width))

    oldFile.close()
    newFile.close()

lineNumberAdd()
