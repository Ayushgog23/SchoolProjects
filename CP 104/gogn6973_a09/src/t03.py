"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ayush Gogne
ID:  169026973
Email:  Gogn6973@mylaurier.ca
__updated__ = "2022-12-04"
-------------------------------------------------------
"""
from functions import file_stats

fh = open("addresses.txt", "r", encoding="utf-8")
ucount, lcount, dcount, wcount = file_stats(fh)
print(f"{ucount},{lcount},{dcount},{wcount}")
fh.close()


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
