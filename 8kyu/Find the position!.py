"""
When provided with a letter, return its position in the alphabet.

Input :: "a"

Output :: "Position of alphabet: 1"

Note: Only lowercased English letters are tested
"""
from string import ascii_letters


def position(letter):
    return f"Position of alphabet: {ascii_letters.find(letter) + 1}"
