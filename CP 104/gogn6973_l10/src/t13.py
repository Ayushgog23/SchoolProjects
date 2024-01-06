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
from functions import file_copy

filename = "words.txt"
fh_1 = open(filename, "r", encoding="utf-8")
filename2 = "new_words.txt"
fh_2 = open(filename2, "w", encoding="utf-8")
file_copy(fh_1, fh_2)
fh_1.close()
fh_2.close()
print(f"done")


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
