"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ayush Gogne
ID:      169026973
Email:   gogn6973@mylaurier.ca
__updated__ = "2023-02-08"
-------------------------------------------------------
"""
# Imports
from utilities import list_test

fh = open("movies.txt","r",encoding = "utf-8")
line = fh.readline()
source = []
while line != "":
    splittedline = line.split("|")
    source.append(int(splittedline[1]))
    line = fh.readline()
list_test(source)



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