# -*- coding: utf-8 -*-

"""
pygsheets.utils
~~~~~~~~~~~~~~~

This module contains utility functions.

"""


def finditem(func, seq):
    """Finds and returns first item in iterable for which func(item) is True.

    """
    return next((item for item in seq if func(item)))


def numericise(value, empty2zero=False):
    """Returns a value that depends on the input string:
        - Float if input can be converted to Float
        - Integer if input can be converted to integer
        - Zero if the input string is empty and empty2zero flag is set
        - The same input string, empty or not, otherwise.

    Executable examples:

    >>> numericise("faa")
    'faa'
    >>> numericise("3")
    3
    >>> numericise("3.1")
    3.1
    >>> numericise("", empty2zero=True)
    0
    >>> numericise("", empty2zero=False)
    ''
    >>> numericise("")
    ''
    >>> numericise(None)
    >>>
    """
    if value is not None:
        try:
            value = int(value)
        except ValueError:
            try:
                value = float(value)
            except ValueError:
                if value == "" and empty2zero:
                    value = 0

    return value


def numericise_all(input, empty2zero=False):
    """Returns a list of numericised values from strings"""
    return [numericise(s, empty2zero) for s in input]
