"""
Given a string made up of letters a, b, and/or c,
switch the position of letters a and b (change a to b and vice versa).
Leave any incidence of c untouched.

Example:

'acb' --> 'bca'
'aabacbaa' --> 'bbabcabb'
"""

def switcheroo(s):
    mapping_dict = {"a": "b", "b": "a"}
    trans_table = str.maketrans(mapping_dict)
    translated_text = s.translate(trans_table)
    return translated_text
