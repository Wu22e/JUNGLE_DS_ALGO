import sys

n,k=map(int,sys.stdin.readline().split())

cirQueue = [i for i in range(1,n+1)]

result = []
index = 0

for i in range(n):
    index += k-1
    if index >= len(cirQueue):
        index %= len(cirQueue)
    result.append(str(cirQueue.pop(index)))

print("<%s>" %(", ".join(result)))