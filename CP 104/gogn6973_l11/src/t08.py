"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ayush Gogne
ID:  169026973
Email:  Gogn6973@mylaurier.ca
__updated__ = "2022-12-02"
-------------------------------------------------------
"""
# Imports
from functions import find_less

matrix = [[8, 2, -3], [7, 4, 4], [-2, -1, 0], [-1, -6, 2]]
n = float(input("Enter the target value: "))
loc = find_less(matrix, n)
print(loc)


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
