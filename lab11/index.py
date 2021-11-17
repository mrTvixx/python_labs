from random import random

arr = [int(random() * 100) for i in range(20)]

summ = sum(arr[:10])
max_value = max(arr[10:])

print(f"Summ: {summ}; max: {max_value}")