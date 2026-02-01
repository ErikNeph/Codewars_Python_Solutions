"""
Given an integer, return a string with dash '-' marks before and after each odd digit,
but do not begin or end the string with a dash mark.

Ex:

274 -> '2-7-4'
6815 -> '68-1-5'
"""

def dashatize(n: int) -> str:
    res = ""
    for char in str(abs(n)):
        if int(char) % 2 == 0:
            res += char
        else:
            res += "-" + char + "-"
    return res.rstrip("-").lstrip("-").replace("--", "-")
