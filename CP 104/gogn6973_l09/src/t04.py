"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ayush Gogne
ID:  169026973
Email:  Gogn6973@mylaurier.ca
__updated__ = "2022-11-18"
-------------------------------------------------------
"""
# Imports
from functions import validate_code


product_code = input("Enter the product code: ")
category, digits, qualifiers = validate_code(product_code)
print(f"({category}, {digits}, {qualifiers})")


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
