"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ayush Gogne
ID:  169026973
Email:  Gogn6973@mylaurier.ca
__updated__ = "2022-12-01"
-------------------------------------------------------
"""
from functions import generate_matrix_num

rows = int(input("Enter the number of rows in the matrix: "))
cols = int(input("Enter the number of cols in the matrix: "))
low = float(input("Enter the low value of the range: "))
high = float(input("Enter the high value of the range: "))
value_type = input("Enter the value type you want (int)(float): ")

matrix = generate_matrix_num(rows, cols, low, high, value_type)
print(f"{matrix}")


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
