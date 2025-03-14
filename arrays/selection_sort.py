
from utils import generate_random_array, display_array


def selection_sort(arr, order = lambda x, y: x > y):
    """
    Selection Sort Algorithm

    Args:
        arr (list): The array to be sorted.
        order (callable): A function that takes two elements and returns True if the first element should come before the second element in the sorted array.

    Returns:
        None: The function sorts the array in-place.
    """
    n = len(arr);
    for i in range(n):
        key_index = i
        for j in range(i + 1, n):
            if order(arr[key_index], arr[j]):
                key_index = j
        arr[key_index], arr[i] = arr[i], arr[key_index]


if __name__ == "__main__":
    arr = generate_random_array(10, 1, 100)
    display_array(arr, "[ORIGINAL] = ")

    selection_sort(arr, lambda x, y: x < y)
    display_array(arr, "[SORTED] = ")
