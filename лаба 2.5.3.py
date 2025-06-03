import random

def generate_even_array(n):
    return sorted([random.randrange(0, 100, 2) for _ in range(n)])