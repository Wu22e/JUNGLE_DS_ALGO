from collections import deque
import sys
y,x,z = map(int,sys.stdin.readline().split())

board = [[list(map(int,sys.stdin.readline().split())) for _ in range(x)] for _ in range(z)]
vis = [[[0]*y for _ in range(x)] for _ in range(z)]

dx = [0, 0, 1, -1, 0, 0]
dy = [0, 0, 0, 0, 1, -1]
dz = [1, -1, 0, 0, 0, 0]

def bfs():
    while queue:
        curZ,curX,curY = queue.popleft()
        vis[curZ][curX][curY] = 1
        for dir in range(6):
            nz = curZ + dz[dir]
            nx = curX + dx[dir]
            ny = curY + dy[dir]
            if nx < 0 or nx >= x or ny < 0 or ny >= y or nz < 0 or nz >=z:
                continue
            if vis[nz][nx][ny] != 0 or board[nz][nx][ny] != 0:
                continue
            board[nz][nx][ny] = board[curZ][curX][curY] + 1
            vis[nz][nx][ny] = 1
            queue.append([nz,nx,ny])

queue = deque()
for i in range(z):
    for j in range(x):
        for k in range(y):
            if board[i][j][k] == 1:
                queue.append([i,j,k])

bfs()

flag = False
maxDay = 0

for i in range(z):
    for j in range(x):
        for k in range(y):
            if board[i][j][k] == 0:
                flag = True
            maxDay = max(maxDay,board[i][j][k])

if flag:
    print(-1)
else:
    print(maxDay-1)