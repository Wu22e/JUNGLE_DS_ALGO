seq1 = input()
seq2 = input()

dp = [[0 for _ in range(len(seq1)+1)] for _ in range(len(seq2)+1)]

for i in range(1, len(seq2)+1):
    for j in range(1, len(seq1)+1):
        if seq2[i-1] == seq1[j-1]: dp[i][j] = dp[i-1][j-1] + 1
        else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(max(max(dp)))
# print(max(map(max, dp)))

