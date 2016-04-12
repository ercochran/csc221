#!/usr/bin/env python3

import hw4_solution as sol
# --------------------------------------------------------------------
# Problem 1
#
# Create a function, is_odd, that takes a number and returns True if
# that number is odd.
#
# Function: is_odd
#
# parameters:
# - number
#
# returns: boolean

def test_is_odd():
    assert sol.is_odd(4) == False
    assert sol.is_odd(3) == True

# --------------------------------------------------------------------
# Problem 2
#
# Create a function, is_even, that takes a number and returns True if
# that number is even.
#
# Function: is_even
#
# parameters:
# - number
#
# returns: boolean


def test_is_even():
    assert sol.is_even(4) == True
    assert sol.is_even(3) == False



# --------------------------------------------------------------------
# Problem 3
#
# Create a function, is_mult_of_four, that takes a number and returns
# True if that number is a multiple of four.
#
# Function: is_mult_of_four
#
# parameters:
# - number
#
# returns: boolean

def test_is_mult_of_four():
    assert sol.is_mult_of_four(12) == True
    assert sol.is_mult_of_four(6) == False





# --------------------------------------------------------------------
# Problem 4
#
# Create a function, is_mult_of_x, that takes a number and a divisor
# and returns True if that number is divisible by divisor
#
# Function: is_mult_of_divisor
#
# parameters:
# - number
# - divisor
#
# returns: boolean


def test_is_mult_of_divisor():
    assert sol.is_mult_of_divisor(12,2) == True
    assert sol.is_mult_of_divisor(6,4) == False




# --------------------------------------------------------------------
# Problem 5
#
# Given a string s, return a string made of the first 2 and the last 2
# chars of the original string, so 'spring' yields 'spng'. However, if
# the string length is less than 2, return instead the empty string.
#
# Function: both_ends
#
# parameters:
# - s
#
# returns: string


def test_both_ends():
    input = [
        ("spring" "spng"),
        ('a' , ""),
        ("", ""),
        ('ab', "abab"),
        ('abc', 'abba'),
        ('abcd', 'abcd'),
     ]
     for arg, output in inputs:
         assert both_ends(arg) == output







    assert sol.is_mult_of_divisor(12,2) == True
  #  assert sol.is_mult_of_divisor(6,4) == False





