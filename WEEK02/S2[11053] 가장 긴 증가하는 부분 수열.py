#1번째 방법, 다이나믹프로그래밍 / O(n^2) 으로 품
import sys

n = int(sys.stdin.readline())

numArr = list(map(int,sys.stdin.readline().split()))

dp = [1] * n

for i in range(n):
    for j in range(i):
        if numArr[i] > numArr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
