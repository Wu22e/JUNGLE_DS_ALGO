n = int(input())

dp_up = [1 for _ in range(n)]
dp_down = [1 for _ in range(n)]
arr = list(map(int, input().split()))

for i in range(n):
    for j in range(i):
        if arr[i]>arr[j]:
            dp_up[i] = max(dp_up[i], dp_up[j]+1)

for i in range(n-1,-1,-1):
    for j in range(n-1,i-1,-1):
        if arr[i]>arr[j]:
            dp_down[i] = max(dp_down[i], dp_down[j]+1)

for i in range(n):
    dp_up[i] = dp_up[i] + dp_down[i]
print(max(dp_up)-1)


