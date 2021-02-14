n = int(input())

dp = [[0 for _ in range(10)] for _ in range(n+1)]

for i in range(10):
    dp[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        dp[i][j] = sum(dp[i-1][:j+1])

ans = 0
for i in range(10):
    ans += dp[n][i]
print(ans%10007)