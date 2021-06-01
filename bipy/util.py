"""
util.py

A collection of misc. utility functions.
"""


import sys


def printerr(*args, **kwargs):
    """
    Print to stderr using the same syntax as the built-in print function.
    """
    print(*args, file=sys.stderr, **kwargs)
