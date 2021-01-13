import sys
from collections import deque

r,c = map(int,sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(r)]
vis_animal = [[0]*c for _ in range(r)]
vis_water = [[0]*c for _ in range(r)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs():
    while Q_water:
        curX ,curY = Q_water.popleft()
        for dir in range(4):
            nx = curX + dx[dir]
            ny = curY + dy[dir]
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            if vis_water[nx][ny] != 0 or board[nx][ny] == 'X' or board[nx][ny] == 'D':
                continue
            vis_water[nx][ny] = vis_water[curX][curY] + 1
            Q_water.append([nx, ny])
    
    while Q_animal:
        curX ,curY = Q_animal.popleft()
        if curX == destinationX and curY == destinationY:
            return vis_animal[curX][curY] - 1
        for dir in range(4):
            nx = curX + dx[dir]
            ny = curY + dy[dir]
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            if vis_animal[nx][ny] != 0 or board[nx][ny] == 'X':
                continue

            vis_animal[nx][ny] = vis_animal[curX][curY] + 1

            if board[nx][ny] == 'D':
                Q_animal.append([nx, ny])
                break

            elif vis_animal[nx][ny] < vis_water[nx][ny] or vis_water[nx][ny] == 0: # 물이 없을때도 가야되는데 이조건을 빼먹어서 계속틀렸음;;;
                Q_animal.append([nx, ny])
            else:
                vis_animal[nx][ny] = 0
    return 'KAKTUS'


Q_water = deque()
Q_animal = deque()
for i in range(r):
    for j in range(c):
        if board[i][j] == 'S':
            Q_animal.append([i, j])
            vis_animal[i][j] = 1
        elif board[i][j] == '*':
            Q_water.append([i, j])
            vis_water[i][j] = 1
        elif board[i][j] == 'D':
            destinationX, destinationY = i, j

print(bfs())
