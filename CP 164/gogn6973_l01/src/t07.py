"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ayush Gogne
ID:      169026973
Email:   gogn6973@mylaurier.ca
__updated__ = "2023-01-19"
-------------------------------------------------------
"""
# Imports
from Movie_utilities import read_movies

fv = open("movies.txt","r",encoding = "utf-8")
movies = read_movies(fv)
print(movies)

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