"""
Write a small function that returns the values of an array that are not odd.

All values in the array will be integers. Return the good values in the order they are given.
"""

def no_odds(values):
    return [even_num for even_num in values if even_num % 2 == 0]
