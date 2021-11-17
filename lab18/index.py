from random import random

matrix = []
rows = int(input("Rows: "))
cols = int(input("Cols: "))

for i in range(rows):
  matrix.append([int(random() * 100) for i in range(cols)])


print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in matrix]))
print("=================")
summ = [sum(i) for i in matrix]
print(f"Summ: {summ}")