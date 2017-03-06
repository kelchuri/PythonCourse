__author__ = 'Kalyan'

notes = '''
Fill up each of this methods so that it does what it is intended to do. Use
only the standard data types we have seen so far and builtin functions.

builtin functions: http://docs.python.org/2/library/functions.html

Do not use any control flow statements (if, for...) in this assignment.
Assume that inputs are valid and of expected type, so no checking required.

use constants from string module (string.XXXX) as required.
'''

from placeholders import *

import string

def get_lower_to_upper_dict():
    """
    returns a dict which contains a mapping from lower case letters to upper case letters
    Hint: see the constants in the string module, and the zip builtin function
    """
    lower = string.lowercase
    upper = string.uppercase
    dict1 = zip(lower,upper)
    dict3 =dict(dict1)
    return dict3

def get_digit_to_string_dict():
    """
    return a dict which maps every digit to its string representation.
    Hint: same as above.
    """

    digit = (0,1,2,3,4,5,6,7,8,9)
    string1=string.digits
    dict2 = zip(digit,string1)
    dict4 = dict(dict2)
    return dict4

three_things_i_learnt = """
-zip function
-conversion of tuples into dictionaries
-use of string constants
"""

time_taken_minutes = 60

def test_lower_to_upper_dict():
    lower_to_upper = get_lower_to_upper_dict()
    assert 26 == len(lower_to_upper)
    for x in lower_to_upper:
        y = lower_to_upper[x]
        assert 1 == len(x)
        assert x.islower()
        assert 1 == len(y)
        assert y.isupper()
        assert x.upper() == y


def test_digit_to_string_dict():
    digit_to_string = get_digit_to_string_dict()
    assert 10 == len(digit_to_string)
    for x in range(0,10):
        assert x in digit_to_string
        assert digit_to_string[x] == str(x)
