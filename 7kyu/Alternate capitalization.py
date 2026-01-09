"""
Given a string, capitalize the letters that occupy even indexes and odd indexes separately,
and return as shown below. Index 0 will be considered even.

For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. See test cases for more examples.

The input will be a lowercase string with no spaces.

Good luck!
"""

def capitalize(s):
    str_even_capitalize = ""
    str_odd_capitalize = ""
    res = []

    for i, char in enumerate(s):
        if i % 2 == 0:
            str_even_capitalize += char.upper()
        else:
            str_even_capitalize += char  
    
    for i, char in enumerate(s):
        if i % 2 != 0:
            str_odd_capitalize += char.upper()
        else:
            str_odd_capitalize += char

    res.append(str_even_capitalize)      
    res.append(str_odd_capitalize)
    return res
