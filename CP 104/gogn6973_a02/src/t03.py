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
# Constants
DAY_DIVIDE = 1000000
MONTH_DIVIDE = 10000
# Input
Date = int(input("Enter a date in the format (DDMMYYYY): "))
# Calculations
day = Date // DAY_DIVIDE
month = Date % DAY_DIVIDE // MONTH_DIVIDE
year = Date % MONTH_DIVIDE

print(f"The reformatted date is: {year:04}/{month:02}/{day:02}")


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
