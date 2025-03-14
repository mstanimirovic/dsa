
import random

def generate_random_array(size, min_val, max_val):
    return [random.randint(min_val, max_val) for _ in range(size)]

def display_array(arr, text):
    print(text, arr, sep="")
