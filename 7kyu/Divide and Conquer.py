"""
Given a mixed array of number and string representations of integers,
add up the non-string integers and subtract the total of the string integers.

Return as a number.
"""

def div_con(x: list) -> int:
    list_strings = [char for char in x if isinstance(char, str)]
    sum_ints = sum([num for num in x if isinstance(num, int)])
    sum_strings = sum(map(int, list_strings))
    return sum_ints - sum_strings
