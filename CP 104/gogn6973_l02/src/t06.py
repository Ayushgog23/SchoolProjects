"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ayush Gogne
ID:  169026973
Email:  Gogn6973@mylaurier.ca
__updated__ = "2022-09-22"
-------------------------------------------------------
"""
# Inputs
Principal = int(input(" Enter Mortgage principal($): "))
Numberofpayments = float(input(" Enter Number of years: "))
Numberofpayments = float(Numberofpayments) * 12
Interest = input("Enter Yearly interest rate(%): ")

# Calculations
Interest = float(Interest) / 100 / 12
Monthlypayments = Principal * (Interest * (1 + Interest) **
                               Numberofpayments) / ((1 + Interest)**Numberofpayments - 1)

# Output
print()
print(f"The monthly payments are: ${Monthlypayments}")


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
