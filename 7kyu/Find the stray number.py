"""
You are given an odd-length array of integers,
in which all of them are the same, except for one single number.

Complete the method which accepts such an array,
and returns that single different number.

The input array will always be valid! (odd-length >= 3)
"""

def stray(arr: list) -> int:
    num1, num2 = set(arr)
    return num1 if arr.count(num1) == 1 else num2
