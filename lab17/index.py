from random import random

matrix = []
rows = int(input("Rows: "))
cols = int(input("Cols: "))
num = int(input("Number: "))

for i in range(rows):
  matrix.append([int(random() * 100) for i in range(cols)])

main_diagonal = []

for idx, _ in enumerate(matrix):
  main_diagonal.append(abs(matrix[idx][idx]))

print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in matrix]))
matrix[num] = [int(i / min(main_diagonal)) for i in matrix[num]]
print("=================")
print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in matrix]))
