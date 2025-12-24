"""
Write a function that returns a string in which firstname is swapped with last name.

Example(Input --> Output)

"john McClane" --> "McClane john"
"""

def name_shuffler(str_) -> str:
    name_shuff = str_.split()
    return " ".join(name_shuff[::-1])
  
