# Write a function that takes in a string o string,
# but with all words that have five or more letters reversed
# (Just like the name of this Kata).
# one or more words, and returns the same. Strings passed in will consist of only letters and spaces.
# Spaces will be included only when more than one word is present.
# Examples:

# "Hey fellow warriors"  --> "Hey wollef sroirraw"
# "This is a test        --> "This is a test"
# "This is another test" --> "This is rehtona test"


def spin_words(sentence):
    return " ".join([i[::-1] if len(i) > 4 else i for i in sentence.split()])
