from itertools import repeat, accumulate

arr_4 = []
arr_6 = []

for i in range(4):
  input_value = input(f'Array(4) element #{i + 1}: ')
  
  try:
    input_value = int(input_value)
    arr_4.append(input_value)
  except:
    print("Unexpected error")
    break

for i in range(6):
  input_value = input(f'Array(4) element #{i + 1}: ')
  
  try:
    input_value = int(input_value)
    arr_6.append(input_value)
  except:
    print("Unexpected error")
    break

print(f"Original (4)): {arr_4}")
print(f"Original (6)): {arr_6}")

arr_final = []

for el in arr_4:
  if el > 0:
    arr_final.append(el)

arr_final.append(arr_6[-1])

print(arr_final)