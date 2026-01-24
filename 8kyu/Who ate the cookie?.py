"""
For this problem you must create a program that says who ate the last cookie.
If the input is a string then "Zach" ate the cookie. If the input is a float or an int then "Monica"
ate the cookie. If the input is anything else "the dog" ate the cookie.
The way to return the statement is: "Who ate the last cookie? It was (name)!"

Ex: Input = "hi" --> Output = "Who ate the last cookie? It was Zach!
(The reason you return Zach is because the input is a string)

Note: Make sure you return the correct message with correct spaces and punctuation.

Please leave feedback for this kata. Cheers!
"""

def cookie(x: str) -> str:
    res = "Who ate the last cookie? It was "
    if isinstance(x, str):
        return res + "Zach!"
    elif isinstance(x, int | float) and not isinstance(x, bool):
        return res + "Monica!"
    else:
        return res + "the dog!"
