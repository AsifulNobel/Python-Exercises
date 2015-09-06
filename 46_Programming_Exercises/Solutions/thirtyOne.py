# Problem Statement
# Implement the higher order functions map(), filter() and reduce().
# (They are built-in but writing them yourself may be a good exercise.)

# These are just partial implementations of the functions
# So there are limitations and shortcomings like this functions
# can work with only one list unlike the actual map, reduce, filter functions

__author__ = "Asiful Nobel"

def myMap(f, lst):
    result = []
    for args in lst:        # returns a list consisting of lst and *lsts
        result.append(f(args))
    return result

def myFilter(f, lst):
    result = []
    for args in lst:
        if f(args):
            result.append(args)
    return result

def myReduce(f, lst):
    result = lst[0]
    for value in lst[1:]:
        result = f(result, value)
    return result


inputList = input("Enter list of strings: ")
# Instead of lambda expression, normal functions can also be passed just like map(), filter(), reduce()
print "Mapped List: {0}".format(myMap(lambda word: len(word), inputList))
print "Filtered List: {0}".format(myFilter(lambda word: len(word) > 3, inputList))
print "Reduced List: {0}".format(myReduce(lambda x,y: x+y, myMap(lambda word: len(word), inputList)))
