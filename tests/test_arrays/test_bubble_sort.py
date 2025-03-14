
from arrays import bubble_sort


def test_bubble_sort():
    arr = [5, 6, 2, 0, -1]
    bubble_sort(arr)
    assert arr == [-1, 0, 2, 5, 6]

def test_bubble_sort_sorted():
    arr = [-1, 0, 2, 5, 6]
    bubble_sort(arr)
    assert arr == [-1, 0, 2, 5, 6]

def test_bubble_sort_descending():
    arr = [3, 2, 1]
    bubble_sort(arr, lambda x, y: x < y)
    assert arr == [3, 2, 1]

def test_bubble_sort_empty():
    arr = []
    bubble_sort(arr)
    assert arr == []

def test_bubble_sort_single_element():
    arr = [1]
    bubble_sort(arr)
    assert arr == [1]
