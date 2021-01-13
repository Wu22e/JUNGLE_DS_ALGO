import sys

N = int(sys.stdin.readline())
conference = []

for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())
    conference.append((start, end))

conference.sort()
result = [conference[0]]

for i in range(1, len(conference)):
    if result[-1][1] > conference[i][1]:
        result.pop()
        result.append(conference[i])
        continue

    if result[-1][1] <= conference[i][0]:
        result.append(conference[i])
        
print(len(result))