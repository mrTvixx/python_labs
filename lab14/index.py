from random import random

summ = 0
matrix = [
  [int(random() * 100) for i in range(3)],
  [int(random() * 100) for i in range(3)],
  [int(random() * 100) for i in range(3)],
]

for arr in matrix:
  for idx, value in enumerate(arr):
    if idx == 2:
      summ += value

summ += sum(matrix[1])

print(f"Summ: {matrix}")