
from arrays import quick_sort


def test_quick_sort():
    arr = [8, 0, -1, 3, 4, 2, 7]
    sorted_arr = quick_sort(arr)
    assert sorted_arr == [-1, 0, 2, 3, 4, 7, 8]


def test_quick_sort_descending():
    # not yet implemented
    pass


def test_quick_sort_empty():
    arr = []
    sorted_arr = quick_sort(arr)
    assert sorted_arr == []


def test_quick_sort_single_element():
    arr = [3]
    sorted_arr = quick_sort(arr)
    assert sorted_arr == [3]
