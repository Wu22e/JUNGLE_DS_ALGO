import sys

input = sys.stdin.readline

n, m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

pSum = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        pSum[i][j] = board[i-1][j-1] + pSum[i-1][j] + pSum[i][j-1] - pSum[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int,input().split())
    if (x1, y1) == (x2, y2):
        print(board[x1-1][y1-1])
    else:
        print(pSum[x2][y2] - pSum[x2][y1-1] - pSum[x1-1][y2] + pSum[x1-1][y1-1])