"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ayush Gogne
ID:  169026973
Email:  Gogn6973@mylaurier.ca
__updated__ = "2022-12-04"
-------------------------------------------------------
"""
# Imports
from functions import file_integers

fh = open("numbers.txt", "r", encoding="utf-8")
numbers = file_integers(fh)
print(f"{numbers}")
fh.close()


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
