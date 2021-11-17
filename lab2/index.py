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

start = int(input('Start index: '))
end = int(input('End index: '))

summ = sum(arr[start: end])

print(summ)
