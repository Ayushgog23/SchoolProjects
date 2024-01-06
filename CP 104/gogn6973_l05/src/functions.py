"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ayush Gogne
ID:  169026973
Email:  Gogn6973@mylaurier.ca
__updated__ = "2022-10-22"
-------------------------------------------------------
"""


def gym_cost(cost, friends):
    """
    -------------------------------------------------------
    Calculates total cost of a gym membership. A member gets a
    discount according to the number of friends they sign up.
        0 friends: 0% discount
        1 friend: 5% discount
        2 friends: 10% discount
        3 or more friends: 15% discount
    Use: final_cost = gym_cost(cost, friends)
    -------------------------------------------------------
    Parameters:
        cost - a gym membership base cost (float > 0)
        friends - number of friends signed up (int >= 0)
    Returns:
        final_cost - cost of membership after discount (float)
    ------------------------------------------------------
    """

    if friends == 1:
        return cost * 0.95
    elif friends == 2:
        return cost * 0.90
    elif friends >= 3:
        return cost * 0.85
    else:
        return cost


def closest(target, v1, v2):
    """
    -------------------------------------------------------
    Determines closest value of two values to a target value.
    Use: result = closest(target, v1, v2)
    -------------------------------------------------------
    Parameters:
        target - the target value (float)
        v1 - first comparison value (float)
        v2 - second comparison value (float)
    Returns:
        result - one of v1 or v2 that is closest to target,
          v1 is the value chosen if v1 and v2 are an equal
          distance from target (float)
    -------------------------------------------------------
    """
    if v1 == v2:
        result = v1
    elif target - v1 < target - v2:
        result = v1
    else:
        result = v2
    return result


def richter(intensity):
    """
    -------------------------------------------------------
    Determines damage level given earthquake intensity measured
    on the Richter scale.
    Use: result = richter(intensity)
    -------------------------------------------------------
    Parameters:
        intensity - Richter scale number for severity of earthquake
            (float >= 0)
    Returns:
        result - description of earthquake damage (str)
    -------------------------------------------------------
    """
    if intensity < 5:
        result = "Little or no damage"
    elif 5 <= intensity < 5.5:
        result = "Some damage"
    elif 5.5 <= intensity < 6.5:
        result = "Serious damage: walls may crack or fall"
    elif 6.5 <= intensity < 7.5:
        result = "Disaster: buildings may collapse"
    elif intensity >= 7.5:
        result = "Catastrophe: most buildings destroyed"
    return result


def pay_raise(status, years, salary):
    """
    -------------------------------------------------------
    Calculates pay raises for employees. Pay raises are based on:
    status: Full Time ('F)' or Part Time ('P')
    and years of service
    Raises are:
        5% for full time greater than or equal to 10 years service
        1.5% for full time less than 4 years service
        3% for part time greater than 10 years service
        1% for part time less than 4 years service
        2% for all others
    Use: new_salary = pay_raise(status, years, salary)
    -------------------------------------------------------
    Parameters:
        status - employment type (str - 'F' or 'P')
        years - number of years employed (int > 0)
        salary - current salary (float > 0)
    Returns:
        new_salary - employee's new salary (float).
    -------------------------------------------------------
    """
    if status == "F" and years >= 10:
        new_salary = salary * 1.05
    elif status == "F" and years < 4:
        new_salary = salary * 1.015
    elif status == "P" and years > 10:
        new_salary = salary * 1.03
    elif status == "P" and years < 4:
        new_salary = salary * 1.01
    else:
        new_salary = salary * 1.02
    return new_salary


def ticket():
    """
    -------------------------------------------------------
    School play ticket price calculation.
    Asks user for their age, and if necessary, if they are
    a student at the school. Prices:
        Infant (age < 3): $0
        Senior (age >= 65): $4.00
        Student (10 <= age < 18): $3.00
            Student of this school: $1.00
        Adult (18 <= age < 65): $5.00
        Kid (3 <= age < 10): $2.00
    Use:   
    -------------------------------------------------------
    Returns:
        price - the price of one ticket (float)
    -------------------------------------------------------
    """

    AGE = int(input("How old are you? "))
    if AGE < 3:
        price = 0
    elif AGE >= 65:
        price = 4
    elif 10 <= AGE < 18:
        choice = input("Are you a student at this school? (Y/N): ")
        if choice == 'Y':
            price = 1
        else:
            price = 3
    elif 18 <= AGE < 65:
        price = 5
    else:
        price = 2
    return price


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
