
from .utils import generate_random_array, display_array


def merge_sort(arr, order = lambda x, y: x > y):
    """
    Merge Sort Algorithm

    Args:
        arr (list): The array to be sorted.
        order (callable): A function that takes two elements and returns True if the first element should come before the second element in the sorted array.

    Returns:
        list: The sorted array.
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid], order)
    right = merge_sort(arr[mid:], order)

    return merge(left, right, order)


def merge(left, right, order = lambda x, y: x > y):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if order(left[i], right[j]):
            merged.append(right[j])
            j += 1
        else:
            merged.append(left[i])
            i += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


if __name__ == "__main__":
    arr = generate_random_array()
    display_array(arr, "[ORIGINAL] = ")

    sorted_arr = merge_sort(arr, lambda x, y: x < y)
    display_array(sorted_arr, "[SORTED] = ")
