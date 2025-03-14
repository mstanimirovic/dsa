
from utils import generate_random_array, display_array


def insertion_sort(arr, order = lambda x, y: x > y):
    """
    Insertion Sort Algorithm

    Args:
        arr (list): The array to be sorted.
        order (callable): A function that takes two elements and returns True if the first element should come before the second element in the sorted array.

    Returns:
        None: The function sorts the array in-place.
    """
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and not order(key, arr[j]):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

if __name__ == "__main__":
    arr = generate_random_array(10, 1, 100)
    display_array(arr, "[ORIGINAL] = ")

    insertion_sort(arr, lambda x, y: x < y)
    display_array(arr, "[SORTED] = ")
