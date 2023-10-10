#!/usr/bin/python3
"""
     A method that calculates the fewest number of operations needed to result.
"""


def minOperations(n):
    """
        A function that calculates the fewest number of operations needed
    """

    present = 1
    start = 0
    count = 0
    while present < n:
        remainder = n - present
        if (remainder % present == 0):
            start = present
            present += start
            count += 2
        else:
            present += start
            count += 1
    return count
