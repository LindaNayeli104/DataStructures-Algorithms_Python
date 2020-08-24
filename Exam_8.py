import random
"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    pivot = random.randrange(0, len(array), 1)
    print(pivot)
    x = array.index(array[pivot])
    print(x)
    """
    for i in range(0, len(array)):
        if array[i] < pivot:
    """


if __name__ == "__main__":
    test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
    print(quicksort(test))