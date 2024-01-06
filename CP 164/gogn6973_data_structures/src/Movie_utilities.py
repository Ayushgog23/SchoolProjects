"""
-------------------------------------------------------
Movie class utility functions.
-------------------------------------------------------
Author:  Ayush Gogne
ID:      169026973
Email:   gogn6973@mylaurier.ca
Section: CP164 
__updated__ = "2021-01-12"
-------------------------------------------------------
"""
from Movie import Movie
from argparse import Action


def get_movie():
    """
    -------------------------------------------------------
    Creates a Movie object by requesting data from a user.
    Use: movie = get_movie()
    -------------------------------------------------------
    Returns:
        movie - a Movie object based upon the user input (Movie).
    -------------------------------------------------------
    """
    title = input("Enter a movie title: ")
    year = int(input("Enter the year of release: "))
    director = input("Enter the name of the director: ")
    rating = float(input("Enter the rating of the movie: "))
    genres = read_genres()
    movie = Movie(title, year, director, rating, genres)


    return movie


def read_movie(line):
    """
    -------------------------------------------------------
    Creates and returns a Movie object from a line of formatted string data.
    Use: movie = read_movie(line)
    -------------------------------------------------------
    Parameters:
        line - a vertical bar-delimited line of movie data in the format
          title|year|director|rating|genre codes (str)
    Returns:
        movie - a Movie object based upon the data from line (Movie)
    -------------------------------------------------------
    """
    splitline = line.split("|")
    title = splitline[0]
    year = int(splitline[1])
    director = splitline[2]
    rating = float(splitline[3])
    # genres
    splitgenres = splitline[4].split(",")
    genres = []
    for i in splitgenres:
        genres.append(int(i))

    
    movie = Movie(title, year, director, rating, genres)

    return movie


def read_movies(fv):
    """
    -------------------------------------------------------
    Reads a file of string data into a list of Movie objects.
    Use: movies = read_movies(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file of movie data (file)
    Returns:
        movies - a list of Movie objects (list of Movie)
    -------------------------------------------------------
    """ #Dellamorte Dellamore|1994|Michele Soavi|7.2|3,4,5,8
    movies = []
    line = fv.readline()
    while line != " ":
        splittedline = line.split("|")
        title = splittedline[0]
        director = splittedline[2]
        rating = float(splittedline[3])
        year = int(splittedline[1])
        splittedgenres = splittedline[4].split(",")
        genres = []
        for i in splittedgenres:
            genres.append(int(i))
        m1 = Movie(title, year, director, rating, genres)
        movies.append(m1)
        line = fv.readline()
        

    return movies


def read_genres():
    """
    -------------------------------------------------------
    Asks a user to select genres from a list of genres and returns
    an integer list of the genres chosen.
    Use: genres = read_genres()
    -------------------------------------------------------
    Returns:
        genres - sorted numeric list of movie genres (list of int)
    -------------------------------------------------------
    """
    s = Movie.genres_menu()
    print(s)
    genres = []
    number = input("Enter a genre number (ENTER to quit): ")
    while genres == [] or number != "":
        r = False
        for i in genres:
            if int(number) == i:
                r = True
            
        if number.isdigit() == False and number != "":
            print("Error: not a positive number")
        elif r == True:
            print("Error: genre already chosen")
        elif int(number) > len(Movie.GENRES)-1:
            print("Error: input must be <= 10")
        elif genres == [] and number == "":
            print("Error: Must have at least one number inside list")
        else:
            integernumber = int(number)
            genres.append(integernumber)
        number = input("Enter a genre number (ENTER to quit): ")   
                       
    genres.sort()


    return genres


def write_movies(fv, movies):
    """
    -------------------------------------------------------
    Writes the contents of movies to fv. Overwrites or
    creates a new file of Movie objects converted to strings.
    Use: write_movies(fv, movies)
    -------------------------------------------------------
    Parameters:
        fv - an already open file of movie data (file)
        movies - a list of Movie objects (list of Movie)
    Returns:
        None
    -------------------------------------------------------
    """

    # Your code here

    return


def get_by_year(movies, year):
    """
    -------------------------------------------------------
    Creates a list of Movies from a particular year.
    The original list of movies must be unchanged.
    Use: ymovies = get_by_year(movies, year)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        year - the Movie year to select (int)
    Returns:
        ymovies - Movie objects whose year attribute is
            year (list of Movie)
    -------------------------------------------------------
    """
    ymovies = []
    for i in range(len(movies)):
        if movies[i].year == year:
            ymovies.append(movies[i])
        
    return ymovies


def get_by_rating(movies, rating):
    """
    -------------------------------------------------------
    Creates a list of Movies whose ratings are equal to or higher
    than rating.
    The original list of movies must be unchanged.
    Use: rmovies = get_by_rating(movies, rating)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        rating - the minimum Movie rating to select (float)
    Returns:
        rmovies - Movie objects whose rating attribute is
            greater than or equal to rating (list of Movie)
    -------------------------------------------------------
    """
    rmovies = []
    for i in range(len(movies)):
        if movies[i].rating >= rating:
            rmovies.append(movies[i])

    return rmovies


def get_by_genre(movies, genre):
    """
    -------------------------------------------------------
    Creates a list of Movies whose list of genres include genre.
    The original list of movies must be unchanged.
    Use: gmovies = get_by_genre(movies, genre)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        genre - the genre code to look for (int)
    Returns:
        gmovies - Movie objects whose genre list includes
            genre (list of Movie)
    -------------------------------------------------------
    """
    gmovies = []
    for i in range(len(movies)):
        for j in range(len(movies[i].genres)):
            if movies[i].genres[j] == genre:
                gmovies.append(movies[i])

    return gmovies


def get_by_genres(movies, genres):
    """
    -------------------------------------------------------
    Creates a list of Movies whose list of genres include all the genre
    codes in genres.
    The original list of movies must be unchanged.
    Use: m = get_by_genres(movies, genres)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        genres - the genre codes to look for (list of int)
    Returns:
        gmovies - Movie objects whose genre list includes
            all the genres in genres (list of Movie)
    -------------------------------------------------------
    """
    
    
    gmovies = []
    for i in range(len(movies)):
        notequalto = []
        equalto = [] 
        for j in movies[i].genres:
            for k in genres:
                if j != k:
                    notequalto.append(j)
                elif j == k:
                    equalto.append(j)
        if equalto == genres and len(notequalto) == 0:
            gmovies.append(movies[i])           
            
    return gmovies


def genre_counts(movies):
    """
    -------------------------------------------------------
    Counts the number of movies in each genre given in Movie.GENRES.
    The original list of movies must be unchanged.
    Use: counts = genre_counts(movies)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
    Returns:
        counts - the number of Movies in each genre in Movie.GENRES.
            The index of each number in counts is the index of
            the matching genre in Movie.GENRES. (list of int)
    -------------------------------------------------------
    """
    #GENRES = ("science fiction", "fantasy", "drama",
        #      "romance", "comedy", "zombie", "action",
        #     "historical", "horror", "war", "mystery")
        
    sciencefiction = 0
    fantasy = 0
    romance = 0
    comedy = 0
    zombie = 0
    action = 0
    historical = 0
    horror = 0
    war = 0
    mystery = 0
    
    for i in range(len(movies)):
        for j in movies[i].genres:
            if j == 0:
                sciencefiction += 1
            elif j == 1:
                fantasy += 1
            elif j == 2:
                romance += 1
            elif j == 3:
                comedy += 1
            elif j == 4:
                zombie += 1
            elif j == 5:
                action += 1
            elif j == 6:
                historical += 1
            elif j == 7:
                horror += 1
            elif j == 8:
                war += 1
            elif j == 9:
                mystery += 1
        
    counts = [int(f"{sciencefiction}"),int(f"{fantasy}"),int(f"{romance}"),int(f"{comedy}"),int(f"{zombie}"),int(f"{action}"),int(f"{historical}"),int(f"{horror}"),int(f"{war}"),int(f"{mystery}")]
    return counts
