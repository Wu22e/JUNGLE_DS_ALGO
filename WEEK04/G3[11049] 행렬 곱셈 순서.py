import sys

n = int(input())

dp =[[0 for _ in range(n)] for _ in range(n)]
matrix = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(n-i):
        dp[j][j+i] = 2**32
        for k in range(j, j+i):
            dp[j][j+i] = min(dp[j][j+i], dp[j][k]+dp[k+1][j+i] + matrix[j][0]*matrix[k][1]*matrix[j+i][1])
print(dp[0][n - 1]) # max(max(dp)) 하면 틀렸다고 나옴