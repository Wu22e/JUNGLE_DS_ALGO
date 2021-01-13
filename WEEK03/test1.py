import sys
from collections import deque

n = int(input())
board = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(n)]
vis = [[0] * n for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

danji = 0
danjiNum = [1]*(n**2)

for i in range(n):
    for j in range(n):
        if board[i][j] == 0 or vis[i][j] == 1: 
            continue

        queue = deque()
        vis[i][j] = 1
        queue.append([i,j])
        while queue:
            curX, curY = queue.popleft()
            for dir in range(4):
                nx = curX + dx[dir]
                ny = curY + dy[dir]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if board[nx][ny] == 0 or vis[nx][ny] == 1:
                    continue
                vis[nx][ny] = 1
                queue.append([nx, ny])
                danjiNum[danji] += 1
        danji += 1

newDanjiNum = []
print(danji)
for i in range(danji):
    newDanjiNum.append(danjiNum[i])
newDanjiNum.sort()
for i in range(danji):
    print(newDanjiNum[i])
