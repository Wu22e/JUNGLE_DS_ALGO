import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(map(int, input().split()))

start = 0
end = 0
sum = 0
result = 0

while start <= n - 1 or end <= n - 1:
    if sum > m:
        sum -= arr[start]
        start += 1

    elif sum < m:
        if end > n - 1:
            break
        sum += arr[end]
        end += 1

    if sum == m:
        result += 1
        if end > n-1:
            sum -= arr[start]
            start += 1
        else:
            sum += arr[end]
            end += 1

print(result)