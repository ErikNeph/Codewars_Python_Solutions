"""
Examples (input -> output)
"c" -> False
"C" -> True
"hello I AM DONALD" -> False
"HELLO I AM DONALD" -> True
"ACSKLDFJSgSKLDFJSKLDFJ" -> False
"ACSKLDFJSGSKLDFJSKLDFJ" -> True

In this Kata, a string is said to be in ALL CAPS whenever it does not
contain any lowercase letter so any string containing no letters at all is trivially considered to be in ALL CAPS.
"""
from string import punctuation


def is_uppercase(inp: str) -> bool:
    return True if inp.isupper() or inp in punctuation or inp.isnumeric() else False
