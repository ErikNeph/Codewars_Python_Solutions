"""
Given the string representations of two integers, return the string representation of the sum of those integers.

For example:

sumStrings('1','2') // => '3'
A string representation of an integer will contain no characters besides the ten numerals "0" to "9".

I have removed the use of BigInteger and BigDecimal in java

Python: your solution need to work with huge numbers (about a milion digits), converting to int will not work.
"""
from itertools import zip_longest


def sum_strings(a: str, b: str) -> str:    
    a = a.lstrip("0") or "0"
    b = b.lstrip("0") or "0"
    
    carry = 0
    result = []
    
    for x, y in zip_longest(reversed(a), reversed(b), fillvalue="0"):
        total = int(x) + int(y) + carry
        digit = total % 10  # остаток от деления на 10
        carry = total // 10  # целая часть от деления на 10
        result.append(str(digit))
    
    if carry:
        result.append(str(carry))
    
    return "".join(result[::-1]).lstrip("0") or "0"
