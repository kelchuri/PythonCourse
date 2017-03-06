__author__ = 'Kalyan'

from placeholders import *

notes = '''
Fill up each of this methods so that it does what it is intended to do. Use
only the standard data types we have seen so far and builtin functions.

builtin functions: http://docs.python.org/2/library/functions.html

Do not use any control flow statements (if, for...) in this assignment.
Assume that inputs are valid and of expected type, so no checking required.
'''


def get_odds_list(count):
    """
     This method returns a list of the first 'count' odd numbers in descending
     order. e.g count = 3 should return [5,3,1]
    """

    odd_list =range(1,(count*2)+1,2)
    odd_list.reverse()
    return odd_list



def get_sorted_diff_string(first, second):
    """
    returns a string which contains letters in first but not in second.
    e.g.s apple and pig returns ael.
    """
    set1 = set(first)
    set2 = set(second)
    diff = set1-set2

    return "".join(sorted(diff))

def get_sorted_without_duplicates(input):
    """
    returns a string in which characters are sorted and duplicates removed
    e.g apple returns aelp, engine returns egin
    """

    return "".join(sorted(set(input)))


three_things_i_learnt = """
-sorting strings
-conversion of one data structure into another
-built in function sorted
"""

time_taken_minutes = 30


def test_odds_list():
    assert [1] == get_odds_list(1)
    assert [] == get_odds_list(0)
    assert [5,3,1] == get_odds_list(3)
    assert [9,7,5,3,1] == get_odds_list(5)

def test_sorted_diff_string():
    assert "" == get_sorted_diff_string("apple", "apple")
    assert "aelp" == get_sorted_diff_string("apple", "")
    assert "do" == get_sorted_diff_string("dog", "pig")
    assert "in" == get_sorted_diff_string("pineapple", "apple")


def test_sorted_without_duplicates():
    assert "aelp" == get_sorted_without_duplicates("apple")
    assert "eorz" == get_sorted_without_duplicates("zeroo")
    assert "" == get_sorted_without_duplicates("")
    assert "abcd" == get_sorted_without_duplicates("abcdabcd")


