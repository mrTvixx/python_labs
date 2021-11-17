from random import random

matrix = [
  [int(random() * 100) for i in range(3)],
  [int(random() * 100) for i in range(3)],
  [int(random() * 100) for i in range(3)],
]
min_value = {'x': 0, 'y': 0}
main_diagonal = []

for idx1, arr in enumerate(matrix):
  for idx2, value in enumerate(arr):
    if value < matrix[min_value['y']][min_value['x']]:
      min_value = { 'x': idx2, 'y': idx1}
    
    if idx1 == idx2:
      main_diagonal.append(value)

print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in matrix]))
matrix[min_value['y']][min_value['x']] = max(main_diagonal)
print("==============")
print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in matrix]))