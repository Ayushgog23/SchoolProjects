"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ayush Gogne
ID:  169026973
Email:  Gogn6973@mylaurier.ca
__updated__ = "2022-09-30"
-------------------------------------------------------
"""
# Inputs
P = float(input("Enter principal amount: "))
r = float(input("Enter the annual rate of interest (as a decimal): "))
t = int(input("Enter number of years the amount is deposited or borrowed for: "))
n = int(input("Enter number of times interest compounded per year: "))
Brackets = 1 + r / n
Exponent = n * t
A = P * Brackets ** Exponent
# Outputs
print(f"Balance: $ {A}")


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
