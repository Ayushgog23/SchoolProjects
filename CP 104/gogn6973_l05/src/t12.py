"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ayush Gogne
ID:  169026973
Email:  Gogn6973@mylaurier.ca
__updated__ = "2022-10-21"
-------------------------------------------------------
"""
# Imports
from functions import pay_raise
# Constants
status = input("employment type (str - 'F' or 'P'): ")
years = int(input("number of years employed (int > 0): "))
salary = float(input("salary (float > 0): "))
new_salary = pay_raise(status, years, salary)
print(f"your new salary is {new_salary:.2f}")


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
