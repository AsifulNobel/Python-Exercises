# The third person singular verb form in English is distinguished by the suffix -s,
# which is added to the stem of the infinitive form: run -> runs. A simple set of
# rules can be given as follows:
#
# If the verb ends in y, remove it and add ies
# If the verb ends in o, ch, s, sh, x or z, add es
# By default just add s
#
# Your task in this exercise is to define a function make_3sg_form() which given a verb
# in infinitive form returns its third person singular form. Test your function with words
# like try, brush, run and fix. Note however that the rules must be regarded as heuristic,
# in the sense that you must not expect them to work for all cases.
# Tip: Check out the string method endswith().
__author__ = "Asiful Nobel"


# Input/Output case has not been handled
def make_3sg_form(input_string):
    # Same thing as the elif condition can be achieved by checking the input_string
    # with re.search(r'[sh|s|o|x|z]', input_string) and if match object is returned,
    # then input_string can be returned as suffixed with 'es'

    if input_string.endswith('y'):
        input_string = input_string[0:-1] + 'ies'
        return input_string
    elif input_string.endswith('o') or \
         input_string.endswith('s') or \
         input_string.endswith('sh') or \
         input_string.endswith('x') or \
         input_string.endswith('z'):
        input_string = input_string + 'es'
        return input_string
    else:
        return (input_string + 's')

print "Plural Form: {0}".format(make_3sg_form(raw_input("Enter Singular Form(lowercase): ")))
