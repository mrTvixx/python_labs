matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9],
]

max_value = 0

for arr in matrix:
  for i in arr:
    if i > max_value: max_value = i

print(f"Max value: {max_value}")