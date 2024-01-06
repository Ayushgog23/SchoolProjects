"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ayush Gogne
ID:  169026973
Email:  Gogn6973@mylaurier.ca
__updated__ = "2022-10-06"
-------------------------------------------------------
"""
# functions

from math import sqrt, pi


def area(radius):
    """
    -------------------------------------------------------
    Calculates and returns area of a circle.
    Use: ar = area(radius)
    -------------------------------------------------------
    Parameters:
        radius - radius of a circle (float >= 0)
    Returns:
        ar - area of a circle (float)
    ------------------------------------------------------
    """
    ar = pi * radius ** 2
    print(f"The area of a circle is: {ar}")
    return ar


def pythag(s1, s2):
    """
    -------------------------------------------------------
    Calculates and returns the radius, diameter, circumference,
    and area of circle defined by a right triangle.
    Use: radius, diam, circ, area = pythag(s1, s2)
    -------------------------------------------------------
    Parameters:
        s1 - length of side 1 of a right triangle (float > 0)
        s2 - length of side 2 of a right triangle (float > 0)
    Returns:
        radius - radius of the resulting circle (float)
        diam - diameter of the resulting circle (float)
        circ - circumference of the resulting circle (float)
        area - area of the resulting circle (float)
    ------------------------------------------------------
    """
    # radius
    radius_inside_calculations = s1 ** 2 + s2 ** 2
    r = sqrt(radius_inside_calculations)
    # Diameter
    Diameter = r * 2
    # Circumference
    Circ = pi * Diameter
    # area
    Area = pi * r ** 2
    print(f"""Radius is: {r}, Diameter is: {Diameter},
    Circumference is {Circ}, Area is {Area}""")
    return r, Diameter, Circ, Area


def fraction_product(num1, den1, num2, den2):
    """
    -------------------------------------------------------
    Calculates and returns fraction values.
    Use: num, den, product = fraction_product(num1, den1, num2, den2)
    -------------------------------------------------------
    Parameters:
        num1 - numerator of first fraction (int)
        den1 - denominator of first fraction (int != 0)
        num2 - numerator of second fraction (int)
        den2 - denominator of second fraction (int != 0)
    Returns:
        num - numerator of product (int)
        den - denominator of product (int)
        product - num / den (float)
    -------------------------------------------------------
    """
    # Calculations
    Num_P = num1 * num2
    Denom_P = den1 * den2
    product = Num_P / Denom_P
    # Print
    print(f"""The numerator of product is {Num_P},
    The denominator of product is {Denom_P}, the product is {product:.2f}""")
    return Num_P, Denom_P, product


def f_to_c(fahrenheit):
    """
    -------------------------------------------------------
    Converts temperatures in fahrenheit to celsius.
    Use: celsius = f_to_c(fahrenheit)
    -------------------------------------------------------
    Parameters:
        fahrenheit - temperature in fahrenheit (int >= -459)
    Returns:
        celsius - equivalent to celsius (float)
    -------------------------------------------------------
    """
    # calculations
    Brackets = fahrenheit - 32
    F_to_C = 5 / 9 * Brackets
    # print
    print(f"the temperature in celsius is: {F_to_C:.2f}")
    return F_to_C


def time_values(SECONDS):
    """
    -------------------------------------------------------
    Returns seconds in different formats.
    Use: days, hours, minutes = time_values(seconds)
    -------------------------------------------------------
    Parameters:
        seconds - total seconds (int >= 0)
    Returns:
        days - number of days in total_seconds (int >= 0)
        hours - number of hours in total_seconds (int >= 0)
        minutes - number of minutes in total_seconds (int >= 0)
    -------------------------------------------------------
    """
    # Calculations
    MINUTES = SECONDS * 0.0166667
    HOURS = MINUTES * 0.0166667
    DAYS = HOURS * 0.0416667
    # print
    print(f"minutes: {MINUTES}, hours: {HOURS}, days: {DAYS}")
    return MINUTES, HOURS, DAYS


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
