"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ayush Gogne
ID:      169026973
Email:   gogn6973@mylaurier.ca
__updated__ = "2023-01-27"
-------------------------------------------------------
"""
# Imports
from utilities import stack_to_array
from utilities import array_to_stack
from Stack_array import Stack

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

target = []
stack_to_array(stack, target)
print(stack)
print(target)



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