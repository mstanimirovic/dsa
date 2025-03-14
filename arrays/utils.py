
import random

def generate_random_array(size = 10, min_val = 0, max_val = 100):
    return [random.randint(min_val, max_val) for _ in range(size)]

def display_array(arr, text = ""):
    print(text, arr, sep="")
