
from utils import generate_random_array, display_array


def bubble_sort(arr, order = lambda x, y: x > y):
    """
    Bubble Sort Algorithm

    Args:
        arr (list): The array to be sorted.
        order (callable): A function that takes two elements and returns True if the first element should come before the second element in the sorted array.

    Returns:
        None: The function sorts the array in-place.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if order(arr[j], arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]


if __name__ == "__main__":
    arr = generate_random_array(10, 1, 100)
    display_array(arr, "[ORIGINAL] = ")
    bubble_sort(arr, lambda x, y: x > y)
    display_array(arr, "[SORTED] = ")
