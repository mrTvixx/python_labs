from random import random

arr = [int(random() * 100) for i in range(200)]
even_arr = []
odd_arr = []

for i in arr:
  if i % 2 == 0:
    even_arr.append(i)
  else:
    odd_arr.append(i)

print(f"Even array: {even_arr}")
print(f"Odd array: {odd_arr}")