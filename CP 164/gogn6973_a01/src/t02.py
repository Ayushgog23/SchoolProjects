"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ayush Gogne
ID:      169026973
Email:   gogn6973@mylaurier.ca
__updated__ = "2023-01-21"
-------------------------------------------------------
"""
# Imports
from functions import file_analyze

filename = input("Enter a filename: ")
fv = open(filename,"r",encoding = "utf-8")
u, l, d, w, r = file_analyze(fv)
fv.close()
print(f"uppercase: {u}")
print(f"lowercase: {l}")
print(f"digits: {d}")
print(f"whitespace: {w}")
print(f"remaining: {r}")


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