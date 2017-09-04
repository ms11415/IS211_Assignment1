#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 1, Part 1"""

class ListDivideException(Exception):
    def __init__(self):
        Exception.__init__(self,'Something went wrong')

def listDivide(numbers, divide=2):
    """Compares numbers in a list with a divisor.

    Args:
        numbers (list): A list of numbers.
        divide (int, optional): The number to divide by. Default: 2

    Returns:
        num_elements (int): The number of elements in the numbers list
        divisible by divide.

   Examples:

        >>> listDivide([1,2,3,4,5])
        2

        >>> listDivide([30, 54, 63, 98, 100], divide=10)
        2
    """
    numcount=0
    for i in numbers:
        if i % divide is 0:
            numcount+=1
    return numcount

def testListDivide():
    """Tests the listDivide function.

    Args:  None.

    Returns:
        ListDivideException if there is a problem; otherwise returns nothing.
    """
    try:
        listDivide([1,2,3,4,5])
        listDivide([2,4,6,8,10])
        listDivide([30, 54, 63,98, 100], divide=10)
        listDivide([])
        listDivide([1,2,3,4,5], 1)
    except:
        raise ListDivideException

testListDivide()
