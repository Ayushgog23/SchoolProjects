"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ayush Gogne
ID:  169026973
Email:  Gogn6973@mylaurier.ca
__updated__ = "2022-10-07"
-------------------------------------------------------
"""
# Inputs
Number = int(input("Enter a positive digit number: "))
# Calculations
One_digit = int(Number % 10)
Other_digits = int(Number // 10)
Product = int(One_digit * Other_digits)
# Output
print(f"The product of the digits {Number} is {Product}")


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
