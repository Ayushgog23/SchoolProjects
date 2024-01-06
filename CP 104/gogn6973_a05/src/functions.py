"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ayush Gogne
ID:  169026973
Email:  Gogn6973@mylaurier.ca
__updated__ = "2022-11-06"
-------------------------------------------------------
"""


def factorial(num):
    """
    -------------------------------------------------------
    Calculates and returns the factorial of num.
    Use: product = factorial(num)
    -------------------------------------------------------
    Parameters:
        num - number to factorial (int > 0)
    Returns:
        product - num! (int)
    ------------------------------------------------------
    """
    product = 1
    for i in range(1, num, 1):
        product += product * i

    return product


def calories_burned(per_minute, minutes):
    """
    -------------------------------------------------------
     prints a table of the number of calories burned 
     every five minutes given the number of calories 
     burned per minute (per_minute) an the total 
     number of minutes run (minutes)
    Use: cal_burns = calories_burned(per_minute, minutes):
    -------------------------------------------------------
    Parameters:
         Per_minute - number of calories burned per minute (float > 0)
         minutes - total number of minutes running 
    Returns:
         cal_burns - total calories burned every 5 minutes
    ------------------------------------------------------
    """

    cal_burns = 0
    for i in range(5, minutes + 1, 5):
        cal_burns = cal_burns + (5 * per_minute)
        print(f"{i}: {cal_burns}")

    return cal_burns


def open_triangle(num_rows):
    """
    -------------------------------------------------------
    takes an integer parameter and prints a triangle 
    of # characters with an empty center.
    Use: triangle = open_triangle(num_rows)
    -------------------------------------------------------
    Parameters:
        num_rows - number of rows to print
    Returns:
        triangle - returns a triangle
    ------------------------------------------------------
    """
    char = "#"
    blank = " "
    for i in range(0, num_rows, 1):
        row = blank * i
        print(f"{char}{row}{char}")

    return row


def multiplication_table(start, stop):
    """
    -------------------------------------------------------
    Prints a multiplication table for values from start to stop.
    Use: multiplication_table(start, stop)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        stop - the range stop value (int)
    Returns:
        None
    ------------------------------------------------------
    """

    for i in range(start, stop + 1):
        print(f"{i:>10d}", end="")
    print(f"\n        ")
    for j in range(start, stop + 1):
        print(f"{j:>6d}|")
        for v in range(start, stop + 1):
            print(f"{j*v:>10d}", end="")
        print()

    return None


def range_total(start, increment, count):
    """
    -------------------------------------------------------
    Uses a for loop to sum count values from start by increment.
    Use: total = range_total(start, increment, count)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        increment - the range increment (int)
        count - the number of values in the range (int)
    Returns:
        total - the sum of the range (int)
    ------------------------------------------------------
    """

    total = 0
    for i in range(count):
        total += (start + i * increment)

    return total


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
