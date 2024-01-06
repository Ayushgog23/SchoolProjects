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
from functions import list_stats
from functions import generate_integer_list

values = generate_integer_list(10, -100, 100)
smallest, largest, total, average = list_stats(values)
print(f"Values: {values}")
print(f"Smallest value: {smallest}")
print(f"Largest value: {largest}")
print(f"Total: {total}")
print(f"Average: {average}")


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
