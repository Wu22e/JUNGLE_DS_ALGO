import sys

n = int(input())

string = list(sys.stdin.readline().split())

cnt = 0
for i in range(n-1):
    if string[i][-1] == string[i+1][0]:
        cnt += 1

if cnt == n-1:
    print(1)
else:
    print(0)

        
