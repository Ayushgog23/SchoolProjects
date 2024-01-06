"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ayush Gogne
ID:  169026973
Email:  Gogn6973@mylaurier.ca
__updated__ = "2022-11-12"
-------------------------------------------------------
"""
# Imports
from functions import generate_integer_list

n = int(input("Enter the number of values to generate: "))
low = int(input("Enter the low value range: "))
high = int(input("Enter the high value range: "))
values = generate_integer_list(n, low, high)
print(f"{values}")


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
