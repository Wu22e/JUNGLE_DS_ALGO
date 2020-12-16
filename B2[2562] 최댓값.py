max = -1

for i in range(9):
    a = int(input())

    if a > max:
        max = a
        index = i+1

print(max)
print(index)
