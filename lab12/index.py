from random import random

count = 0
arr = [int(random() * 100) for i in range(31)]

avarage = sum(arr) / len(arr)

for i in arr:
  if i < avarage:
    count = count + 1

print(f"Count: {count}")