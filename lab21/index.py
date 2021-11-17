from random import random
from functools import reduce

matrix = []
rows = int(input("Rows: "))
cols = int(input("Cols: "))

for i in range(rows):
  matrix.append([int(random() * 100) for i in range(cols)])

sub_diagonal = []

for idx, _ in enumerate(matrix):
  sub_diagonal.append(abs(matrix[idx][cols - 1 - idx]))

print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in matrix]))
print("=================")
print(sub_diagonal)
print("=================")
res = int(reduce(lambda acc, value: acc * value, sub_diagonal) / max(sub_diagonal))
print(f"Result: {res}")