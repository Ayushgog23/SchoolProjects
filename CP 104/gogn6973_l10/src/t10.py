"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ayush Gogne
ID:  169026973
Email:  Gogn6973@mylaurier.ca
__updated__ = "2022-11-26"
-------------------------------------------------------
"""
# Imports
from functions import count_frequency_word

word = input("What word you are searching for: ")
filename = "words.txt"
fh = open(filename, "r", encoding="utf-8")
count = count_frequency_word(fh, word)
fh.close()
print(f"{word} appears {count} times")


def func():
    """
    -------------------------------------------------------
    description
    Use: 
    -------------------------------------------------------
    Parameters:
        name - description (type)
    Returns:
        name - description (type)
    ------------------------------------------------------
    """
