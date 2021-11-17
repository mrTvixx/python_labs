from random import random

matrix = [
  [int(random() * 100) for i in range(3)],
  [int(random() * 100) for i in range(3)],
  [int(random() * 100) for i in range(3)],
]
new_matrix = []

main_diagonal = []

for idx, _ in enumerate(matrix):
  main_diagonal.append(abs(matrix[idx][idx]))

for arr in matrix:
  new_matrix.append([int(i / max(main_diagonal)) for i in arr])

print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in matrix]))
print("=================")
print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in new_matrix]))