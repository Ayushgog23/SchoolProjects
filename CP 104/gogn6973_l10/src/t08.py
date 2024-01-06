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
from functions import append_increment

filename = "numbers.txt"
fh = open(filename, "r+", encoding="utf-8")
number = append_increment(fh)
fh.close()
print(f"{number}\n")


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
