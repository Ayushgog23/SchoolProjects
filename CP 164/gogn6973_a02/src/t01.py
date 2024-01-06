"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ayush Gogne
ID:      169026973
Email:   gogn6973@mylaurier.ca
__updated__ = "2023-01-26"
-------------------------------------------------------
"""
# Imports
from Movie_utilities import get_by_year
from Movie import Movie

movies = []
movies.append(Movie("Spider man",2004,"idk",3.5,[0,2]))
movies.append(Movie("Sonic",2015,"Man",4.5,[0,3]))
movies.append(Movie("Superman",2015,"what",2.5,[1,3]))
year = int(input("Enter a year: "))
ymovies = get_by_year(movies, year)
print(ymovies)






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