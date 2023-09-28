#!/usr/bin/python3
"""peak-finding algorithm."""


def find_peak(list_of_integers):
    """
    Find a peak element in an unsorted list of integers using a recursive algorithm.

    Args:
        arr (list of int): A list of unsorted integers.

    Returns:
        int or None: The peak element if found, None if the list is empty or no peak is present.
    """
    if list_of_integers == []:
        return None

    size = len(list_of_integers)
    if size == 1:
        return list_of_integers[0]
    elif size == 2:
        return max(list_of_integers)

    mid = int(size / 2)
    peak = list_of_integers[mid]
    if peak > list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
        return peak
    elif peak < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
