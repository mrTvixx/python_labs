from math import factorial

arr = []
count = 0

for i in range(7):
  input_value = input(f'Element #{i + 1}: ')
  
  try:
    input_value = int(input_value)
    arr.append(input_value)
    if input_value == 7: count = count + 1
  except:
    print("Unexpected error")
    break

print(f"Array: {arr}")

if count != 0:
  print(f"Count: {count}, factorial: {factorial(count)}")
else:
  print("No expected elements")
