arr = []
positive_arr = []
negative_arr = []

for i in range(10):
  input_value = input(f'Element #{i + 1}: ')
  
  try:
    input_value = int(input_value)
    arr.append(input_value)
  except:
    print("Unexpected error")
    break

print(f"Original array: {arr}")

for i in arr:
  if i > 0:
    positive_arr.append(i)
  else:
    negative_arr.append(i)

print(f"Positive array: {positive_arr}")
print(f"Negative array: {negative_arr}")