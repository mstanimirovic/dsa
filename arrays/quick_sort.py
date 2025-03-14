
from .utils import generate_random_array, display_array


def quick_sort(arr):
    """
    Quick Sort Algorithm

    Args:
        arr (list): The array to be sorted.

    Returns:
        list: The sorted array.
    """
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    left = []
    same = []
    right = []

    for el in arr:
        if el == pivot:
            same.append(el)
        elif el > pivot:
            right.append(el)
        else:
            left.append(el)

    left_arr = quick_sort(left)
    right_arr = quick_sort(right)

    return left_arr + same + right_arr


if __name__ == "__main__":
    arr = generate_random_array()
    display_array(arr, "[ORIGINAL] = ")

    sorted_arr = quick_sort(arr)
    display_array(sorted_arr, "[SORTED] = ")
