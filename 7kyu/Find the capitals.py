# Write a function that takes a single non-empty string of only
# lowercase and uppercase ascii letters (word) as its argument,
# and returns an ordered list containing the indices of all capital (uppercase) letters in the string.
# Example (Input --> Output)
# "CodEWaRs" --> [0,3,4,6]
def capitals(word: str) -> list:
    lst_of_capitals = []
    for index, char in enumerate(word):
        if char.isupper():
            lst_of_capitals.append(index)
    return lst_of_capitals
