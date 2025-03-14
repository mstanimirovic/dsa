
from arrays import insertion_sort


def test_insertion_sort():
    arr = [8, 0, -1, 3, 4, 2, 7]
    insertion_sort(arr)
    assert arr == [-1, 0, 2, 3, 4, 7, 8]


def test_insertion_sort_empty():
    arr = []
    insertion_sort(arr)
    assert arr == []


def test_insertion_sort_single_element():
    arr = [1]
    insertion_sort(arr)
    assert arr == [1]


def test_insertion_sort_sorted():
    arr = [-1, 0, 2, 5, 6]
    insertion_sort(arr)
    assert arr == [-1, 0, 2, 5, 6]


def test_insertion_sort_descending():
    arr = [3, 2, 1]
    insertion_sort(arr, lambda x, y: x < y)
    assert arr == [3, 2, 1]
