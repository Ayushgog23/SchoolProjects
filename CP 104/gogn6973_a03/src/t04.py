"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ayush Gogne
ID:  169026973
Email:  Gogn6973@mylaurier.ca
__updated__ = "2022-10-22"
-------------------------------------------------------
"""
# Imports
from functions import multiply_fractions

num1 = int(input("Numerator of the first fraction (int): "))
denom1 = int(input("Denominator of the first fraction(int): "))
num2 = int(input("Numerator of the second fraction(int): "))
denom2 = int(input("Denominator of the second fraction(int): "))
numerator, denominator, product = multiply_fractions(
    num1, denom1, num2, denom2)
print(f"result: {numerator}/{denominator} = {product:2f}")


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
