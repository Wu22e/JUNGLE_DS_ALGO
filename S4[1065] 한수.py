import sys

n = int(sys.stdin.readline())
cnt = 0

if n//100 >= 1:
    cnt = 99
    for i in range(n-100+1):
        n = 100+i
        d = n%100//10 - n//100
        if n%100//10 + d == n % 10:
            cnt = cnt + 1 
elif n>>10 >=1:
    cnt = 9
    cnt = cnt + n - 10 - 1
else : 
    cnt = n

print(cnt)