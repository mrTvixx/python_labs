result = 0

for i in range(30, 80):
  if i % 2 != 0:
    result += i * i

print(f"Result: {result}")