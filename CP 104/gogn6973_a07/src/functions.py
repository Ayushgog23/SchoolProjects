"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ayush Gogne
ID:  169026973
Email:  Gogn6973@mylaurier.ca
__updated__ = "2022-11-21"
-------------------------------------------------------
"""


def list_factors(num):
    """
   -------------------------------------------------------
   Description: list factors takes in an integer greater than 0 and returns 
   the factors of that integer in the form of a list
   Use: factors = list_factors(num)
   -------------------------------------------------------
   Parameters:
       num - a number greater than 0 (int)
   Returns:
       factors - returns a list of factors (int)
   ------------------------------------------------------
   """

    factors = []
    for i in range(1, num + 1):
        if(num % i == 0):
            factors.append(i)

    factors.pop()

    return factors


def list_positives():
    """
    -------------------------------------------------------
    Gets a list of positive numbers from a user.
    Negative numbers are ignored. Enter 0 to stop entries.
    Use: numbers = list_positives()
    -------------------------------------------------------
    Returns:
        numbers - A list of positive integers (list of int)
    ------------------------------------------------------
    """
    list = int(input("Enter a series of positive numbers (int): "))
    numbers = []
    while list != 0:
        if list > 0:
            numbers.append(list)
        list = int(input("Enter a series of positive numbers (int): "))

    return numbers


def list_indexes(values, target):
    """
    -------------------------------------------------------
    Finds the indexes of target in values.
    Use: indexes = list_indexes(values, target)
    -------------------------------------------------------
    Parameters:
        values - list of value (list of int)
        target - value to look for in num_list (int)
    Returns:
        locations - list of indexes of target (list of int)
    -------------------------------------------------------
    """
    indexes = []

    for i in range(len(values)):
        if values[i] == target:
            indexes.append(i)

    return indexes


def subtract_lists(minuend, subtrahend):
    """
    -------------------------------------------------------
    Updates the list minuend removing from it the values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are not included in the updated list.
    subtrahend is unchanged
    Use: subtract_lists(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to remove from minuend (list)
    Returns:
        None
    ------------------------------------------------------
    """
    index = []

    count = 0
    d = len(minuend)
    a = len(subtrahend)
    for i in range(a):
        for v in range(d):
            if minuend[v] == subtrahend[i]:
                index.append(v)
    for j in index:
        c = j - count
        minuend.pop(c)
        count = count + 1


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
