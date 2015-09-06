# In English, the present participle is formed by adding the suffix -ing to the infinite form:
# go -> going. A simple set of heuristic rules can be given as follows:
#
#     If the verb ends in e, drop the e and add ing (if not exception: be, see, flee, knee, etc.)
#     If the verb ends in ie, change ie to y and add ing
#     For words consisting of consonant-vowel-consonant, double the final letter before adding ing
#     By default just add ing
# Your task in this exercise is to define a function make_ing_form() which given a verb in
# infinitive form returns its present participle form. Test your function with words such as
# lie, see, move and hug. However, you must not expect such simple rules to work for all cases.

__author__ = "Asiful Nobel"


import string, re

def make_ing_form(input_string):
    vowels = 'aeiou'
    consonants = ''.join(set(string.lowercase) - set(vowels))
    pattern = '[' + consonants + ']' + '[' + vowels + ']' + '[' + consonants + ']$'
    exceptionStrings = ['see', 'be', 'flee', 'knee']

    if input_string in exceptionStrings:
        return input_string + 'ing'
    elif input_string.endswith('ie'):
        return input_string[0:-2] + 'ying'
    elif input_string.endswith('e'):
        return input_string[0:-1] + 'ing'
    elif re.search(pattern, input_string):
        return input_string + input_string[-1] + 'ing'
    else:
        return input_string + 'ing'

print "Present participle: {0}".format(make_ing_form(raw_input('Enter string: ').lower()))
