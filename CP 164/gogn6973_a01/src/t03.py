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
from functions import find_subs

string = input("Enter a string to evaluate: ")
sub = input("Enter a sustring to search for: ")
locations = find_subs(string, sub)
print(locations)

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