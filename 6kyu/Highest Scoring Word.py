"""
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

For example, the score of abad is 8 (1 + 2 + 1 + 4).

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.

"""

def high(x: str) -> str:
    list_words = x.split()
    sum_scores = [sum([ord(char)-96 for char in ele])for ele in list_words]
    dict_words_scores = dict(zip(list_words, sum_scores))
    return max(dict_words_scores, key=dict_words_scores.get)
