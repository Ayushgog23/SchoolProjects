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
from functions import mow_lawn

width = float(input("width of a lawn in metres (float > 0): "))
length = float(input("length of a lawn in metres (float > 0): "))
speed = float(input("square metres cut per minute (float > 0): "))
time = mow_lawn(width, length, speed)
print(f"Mowing the lawn takes {time} minutes")


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
