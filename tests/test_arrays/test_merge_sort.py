
from arrays import merge_sort


def test_merge_sort():
    arr = [8, 0, -1, 3, 4, 2, 7]
    sorted_arr = merge_sort(arr)
    assert sorted_arr == [-1, 0, 2, 3, 4, 7, 8]


def test_merge_sort_descending():
    arr = [-1, -1, 2, 4, 4, 7, 9]
    sorted_arr = merge_sort(arr, lambda x, y: x < y)
    assert sorted_arr == [9, 7, 4, 4, 2, -1, -1]


def test_merge_sort_empty():
    arr = []
    sorted_arr = merge_sort(arr)
    assert sorted_arr == []


def test_merge_sort_single_element():
    arr = [3]
    sorted_arr = merge_sort(arr)
    assert sorted_arr == [3]
