
from arrays import selection_sort


def test_selection_sort():
    arr = [8, 0, -1, 3, 4, 2, 7]
    selection_sort(arr)
    assert arr == [-1, 0, 2, 3, 4, 7, 8]

def test_selection_sort_empty():
    arr = []
    selection_sort(arr)
    assert arr == []

def test_selection_sort_single_element():
    arr = [5]
    selection_sort(arr)
    assert arr == [5]

def test_selection_sort_sorted():
    arr = [-1, 0, 2, 3, 4, 7, 8]
    selection_sort(arr)
    assert arr == [-1, 0, 2, 3, 4, 7, 8]

def test_selection_sort_descending():
    arr = [-1, 0, 2, 3, 4, 7, 8]
    selection_sort(arr, lambda x, y: x < y)
    assert arr == [8, 7, 4, 3, 2, 0, -1]
