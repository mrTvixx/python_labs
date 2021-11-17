arr = []

for i in range(10):
  input_value = input(f'Element #{i + 1}: ')
  
  try:
    input_value = int(input_value)
    arr.append(input_value)
  except:
    print("Unexpected error")
    break

print(f"Original array: {arr}")

min_index, max_index = arr.index(min(arr)), arr.index(max(arr))
arr[min_index], arr[max_index] = arr[max_index], arr[min_index]

print(f"Final array: {arr}")
