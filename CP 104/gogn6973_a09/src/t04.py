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
from functions import number_lines

fh_in = open("wilde.txt", "r", encoding="utf-8")
fh_out = open("wilde_numbered.txt", "w", encoding="utf-8")
number_lines(fh_in, fh_out)
fh_in.close()
fh_out.close()


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
