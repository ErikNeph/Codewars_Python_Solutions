"""
Description:
In this Kata, you will be given a string that may have mixed uppercase and
lowercase letters and your task is to convert that string to either lowercase only or uppercase only based on:

make as few changes as possible.
if the string contains equal number of uppercase and lowercase letters, convert the string to lowercase.
For example:

solve("coDe") = "code". Lowercase characters > uppercase. Change only the "D" to lowercase.
solve("CODe") = "CODE". Uppercase characters > lowecase. Change only the "e" to uppercase.
solve("coDE") = "code". Upper == lowercase. Change all to lowercase.
More examples in test cases. Good luck!
"""
def solve(s):
    lower_char = 0
    upper_char = 0

    for char in s:
        if char.islower():
            lower_char += 1
        else:
            upper_char += 1

    return s.lower() if lower_char > upper_char or lower_char == upper_char else s.upper()
