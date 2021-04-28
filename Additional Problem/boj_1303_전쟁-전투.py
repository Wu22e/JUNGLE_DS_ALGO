import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
# print(n,m)
board = [list(input().strip()) for _ in range(m)]
vis = [[0 for _ in range(n)] for _ in range(m)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

result = [0, 0]

def bfs(i, j, target, nontarget):
    if vis[i][j] == 0 and board[i][j] == target:
        queue = deque()
        queue.append([i,j])
        vis[i][j] = 1
        cnt = 1
        while queue:
            curX, curY = queue.popleft()
            for i in range(4):
                nx = curX + dx[i]
                ny = curY + dy[i]
                if nx < 0 or ny < 0 or nx >= m or ny >= n:
                    continue
                if vis[nx][ny] != 0:
                    continue
                if board[nx][ny] == nontarget:
                    continue
                vis[nx][ny] = 1
                cnt += 1
                queue.append([nx,ny])
        return cnt*cnt
    else:
        return 0

for i in range(m):
    for j in range(n):
        if board[i][j] == 'W':
            val = bfs(i,j,'W','B')
            result[0] += val
        else:
            val = bfs(i,j,'B','W')
            result[1] += val
        
print(result[0], result[1])
