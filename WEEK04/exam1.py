import sys
input = sys.stdin.readline

n = int(input())

score = []
for _ in range(n):
    score.append(int(input()))

if n == 1:
    print(score[0])
    exit()

dp = [[0 for _ in range(len(score)+1)] for _ in range(n)] # dp[i][j] , j 크기는 2(뛸 수 있는 점프의 수) , 0번째 인덱스 무시

dp[0][0] = score[0]
dp[1][0] = score[1]
dp[1][1] = score[0] + score[1]

for i in range(2, n):
    dp[i][0] = max(dp[i-2][0], dp[i-2][1]) + score[i]
    dp[i][1] = dp[i-1][0] + score[i]

print(max(dp[n-1][0],dp[n-1][1]))


