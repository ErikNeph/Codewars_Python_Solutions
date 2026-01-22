"""
Implement String#digit? (in Java StringUtils.isDigit(String)),
which should return true if given object is a single digit (0-9), false otherwise.
"""

def is_digit(n):
    return n[0].isdigit() and len(n) <= 1 if n else False
