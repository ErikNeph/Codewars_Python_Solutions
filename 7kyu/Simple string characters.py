"""
In this Kata, you will be given a string and your task will be to return
a list of ints detailing the count of uppercase letters, lowercase,
numbers and special characters (everything else), as follows.

The order is: uppercase letters, lowercase letters, numbers and special characters.

"*'&ABCDabcde12345" --> [ 4, 5, 5, 3 ]
More examples in the test cases.

Good luck!
"""
from string import punctuation


def solve(s: str) -> list[int]:
    upper_chars = 0
    lower_chars = 0
    digits = 0
    spec_symbols = 0
    
    for char in s:
        if char.isupper():
            upper_chars += 1
        if char.islower():
            lower_chars += 1
        if char.isdigit():
            digits += 1
        if char in punctuation:
            spec_symbols += 1

    return [upper_chars, lower_chars, digits, spec_symbols]
