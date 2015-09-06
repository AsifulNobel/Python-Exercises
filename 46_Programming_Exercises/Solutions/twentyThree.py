# Define a simple "spelling correction" function correct() that takes a string and sees
# to it that 1) two or more occurrences of the space character is compressed into one,
# and 2) inserts an extra space after a period if the period is directly followed by a
# letter. E.g. correct("This   is  very funny  and    cool.Indeed!") should return
# "This is very funny and cool. Indeed!" Tip: Use regular expressions!
__author__ = "Asiful Nobel"

def correct(input_string):
    clear_string = ' '.join(input_string.split())
    punctuations = ".,;?!"

    for element in punctuations:
        if element in clear_string:
            case1 = ' ' + element
            case2 = ' ' + element + ' '
            case3 = element + ' '
            clear_string = clear_string.replace(element, case3)
            clear_string = clear_string.replace(case1, case3)
            clear_string = clear_string.replace(case2, case3)

    return clear_string

print "Corrected String: {0}".format(correct(raw_input("Enter a string for correction: ")))
