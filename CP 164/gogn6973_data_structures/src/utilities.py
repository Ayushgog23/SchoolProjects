"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ayush Gogne
ID:      169026973
Email:   gogn6973@mylaurier.ca
__updated__ = "2023-01-25"
-------------------------------------------------------
"""
from Stack_array import Stack
from Movie_utilities import read_movie

def array_to_stack(stack, source):
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last value in source is at bottom of stack,
    first value in source is on top of stack.
    Use: array_to_stack(stack, source)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """                                 
    while len(source) != 0:
        lastvalue = source[len(source)-1]
        stack.push(lastvalue)
        source.pop()
        
    return None

def stack_to_array(stack, target):
    """
    -------------------------------------------------------
    Pops contents of stack into target. At finish, stack is empty.
    Top value of stack is at end of target,
    bottom value of stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    while not stack.is_empty():
        value = stack.peek()
        target.insert(0,value)
        stack.pop()
        
    return None
    

def stack_test(source):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and
    non-empty stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        empty, push, pop, peak
    -------------------------------------------------------
    """
    s = Stack()
    array_to_stack(s, source)
    empty = s.is_empty()
    peek = s.peek()
    push = s.push(4)
    pop = s.pop()
    
    return empty, push, peek, source
    
def stack_test_movies(fv):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and
    non-empty stacks using the data in movies:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test_movies(fv)
    -------------------------------------------------------
    Parameters:
        fv - file with movie data
    Returns:
        peek, empty
    -------------------------------------------------------
    """
    s = Stack()
    line = fv.readline()
    while line != " ":
        movie = read_movie(line)
        s.push(movie)
        line = fv.readline()
    empty = s.is_empty()
    s.pop()
    peek = s.peek()
    
    return empty, peek, list
    
    
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