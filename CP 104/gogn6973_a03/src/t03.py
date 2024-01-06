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
from functions import date_extract

date_number = int(input("A date number in the format MMDDYYYY (int > 0):  "))
year, month, day = date_extract(date_number)
print(f"The reformatted date is: {year}/{month}/{day}")


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
