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
from Movie_utilities import get_by_genres
from Movie import Movie

movies = []
movies.append(Movie("Spider man",2004,"idk",3.5,[0,1,3]))
movies.append(Movie("Sonic",2015,"Man",4.5,[0,1,3]))
movies.append(Movie("Superman",2015,"what",2.5,[1,3]))
genre = int(input("Enter the genre codes to look for: "))
genres = []
while genre != 11:
    genres.append(genre)
    genre = int(input("Enter the genre codes to look for: "))
gmovies = get_by_genres(movies, genres)
print(gmovies)

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