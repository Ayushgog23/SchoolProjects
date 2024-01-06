"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ayush Gogne
ID:  169026973
Email:  Gogn6973@mylaurier.ca
__updated__ = "2022-10-30"
-------------------------------------------------------
"""


def day_of_week(day_number):
    """
    -------------------------------------------------------
    description: function asks for a number and corresponds a 
    day of the week to it
            1 = "Monday"
            2 = "Tuesday
            3 = "Wednesday"
            4 = "Thursday"
            5 = "Friday"
            6 = "Saturday"
            7 = "Sunday"
            returns "error" if any number not listed is inputted
    Use: dayoftheweek = day_of_week(day_number)
    -------------------------------------------------------
    Parameters:
        day_number: a number that will correspond to a day of the week (int)
    Returns:
        dayoftheweek: the day of the week based of the day_number provided (str)
    ------------------------------------------------------
    """

    if day_number == 1:
        dayoftheweek = "Monday"
    elif day_number == 2:
        dayoftheweek = "Tuesday"
    elif day_number == 3:
        dayoftheweek = "Wednesday"
    elif day_number == 4:
        dayoftheweek = "Thursday"
    elif day_number == 5:
        dayoftheweek = "Friday"
    elif day_number == 6:
        dayoftheweek = "Saturday"
    elif day_number == 7:
        dayoftheweek = "Sunday"
    else:
        dayoftheweek = "Error"
    return dayoftheweek


def pollution_level(aqi):
    """
    -------------------------------------------------------
    Returns the pollution level given an AQI (Air Quality Index):
        "Good" - 0 to 50 AQI
        "Moderate" - 51 - 100 AQI
        "Unhealthy for Sensitive Groups" - 101 - 150 AQI
        "Unhealthy" - 151 - 200 AQI
        "Very Unhealthy" - 201 - 300 AQI
        "Hazardous" - 300+ AQI
    Returns "Error" if aqi is negative.
    Use: level = pollution_level(aqi)
    -------------------------------------------------------
    Parameters:
        aqi - Air Quality Index (int)
    Returns:
        level - name of pollution level (str)
    ------------------------------------------------------
    """

    if aqi >= 0 and aqi <= 50:
        level = "Good"
    elif aqi < 0:
        level = "Error"
    elif aqi <= 100:
        level = "Moderate"
    elif aqi <= 150:
        level = "Unhealthy for senstive groups"
    elif aqi <= 200:
        level = "Unhealthy"
    elif aqi <= 300:
        level = "Very unhealthy"
    elif aqi > 300:
        level = "Hazardous"
    return level


def product_largest(v1, v2, v3):
    """
    -------------------------------------------------------
    Returns the product of the two largest values of
    v1, v2, and v3.
    Use: product = product_largest(v1, v2, v3)
    -------------------------------------------------------
    Parameters:
        v1 - a number (float)
        v2 - a number (float)
        v3 - a number (float)
    Returns:
        product - the product of the two largest values of
            v1, v2, and v3 (float)
    ------------------------------------------------------
    """
    if v1 and v2 > v3:
        product = v1 * v2
    elif v1 and v3 > v1:
        product = v2 * v3
    elif v2 and v3 > v1:
        product = v2 * v3
    return product


def rgb_mix(rgb1, rgb2):
    """
    -------------------------------------------------------
    Determines the secondary colour from mixing two primary
    RGB (Red, Green, Blue) colours. The order of the colours
    is *not* significant.
    Returns "Error" if any of the colour parameter(s) are invalid.
        "red" + "blue": "fuchsia"
        "red" + "green": "yellow"
        "green" + "blue": "aqua"
        "red" + "red": "red"
        "blue" + "blue": "blue"
        "green" + "green": "green"
    Use: colour = rgb_mix(rgb1, rgb2)
    -------------------------------------------------------
    Parameters:
        rgb1 - a primary RGB colour (str)
        rgb2 - a primary RGB colour (str)
    Returns:
        colour - a secondary RGB colour (str)
    -------------------------------------------------------
    """
    if rgb1 == "red" and rgb2 == "blue":
        colour = "fushcia"
    elif rgb1 == "red" and rgb2 == "green":
        colour = "yellow"
    elif rgb1 == "red" and rgb2 == "red":
        colour = "red"
    elif rgb1 == "blue" and rgb2 == "blue":
        colour = "blue"
    elif rgb1 == "green" and rgb2 == "green":
        colour = "green"
    else:
        colour = "Error"

    return colour


def yee_ha(number):
    """
    -------------------------------------------------------
    description: takes an integer parameter and returns the following:
        "Yee" if number is evenly divisible by 3
        "Ha" if number is evenly divisible by 7
        "Yee Ha" if number is evenly divisible by both 3 and 7
        "Nada" if number is none of the above
    Use: word = yee_ha(number)
    -------------------------------------------------------
    Parameters:
        number - takes in a number (int)
    Returns: 
        word - a string based on what the number provided is divisible by (str)
    ------------------------------------------------------
    """
    if number % 3 == 0 and number % 7 == 0:
        word = "Yee Ha"
    elif number % 3 == 0:
        word = "Yee"
    elif number % 7 == 0:
        word = "Ha"
    else:
        word = "Nada"
    return word


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
