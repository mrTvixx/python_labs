from random import random

matrix = []
rows = int(input("Rows: "))
cols = int(input("Cols: "))
row_num = int(input("Row for 2: "))

for idx1, _ in enumerate(range(rows)):
  row = []
  for idx2, _ in enumerate(range(cols)):
    if idx1 == idx2:
      row.append(1)
    elif idx1 == row_num:
      row.append(2)
    else:
      row.append(0)
  
  matrix.append(row)

print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in matrix]))