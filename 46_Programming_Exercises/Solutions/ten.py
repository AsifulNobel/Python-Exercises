# Problem Statement
# Write a function overlapping() that takes two lists and returns
# True if they have at least one member in common, False otherwise.
# You may use your is_member() function, or the in operator, but for
# the sake of the exercise, you should also write it using two nested
# for-loops

__author__ = "Asiful Nobel"

def overlapping(list1, list2):
    for value in list1:
        for x in list2:
            if value == x:
                return True
    return False

print "Does the two lists overlap? %s"  %overlapping(input("Enter the first list: "), \
                                                    input("Enter the second list: "))
