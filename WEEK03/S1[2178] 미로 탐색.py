n,m = map(int,input().split())
board = [list(map(int,input())) for _ in range(n)]
vis = [[0] * m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x,y):
    queue = [[x,y]]
    vis[x][y] = 1
    while queue:
        curX,curY = queue.pop(0)

        if curX == n-1 and curY == m-1:
            return(vis[curX][curY])

        for dir in range(4):
            nx = curX + dx[dir]
            ny = curY + dy[dir]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if vis[nx][ny] != 0 or board[nx][ny] == 0:
                continue
            vis[nx][ny] = vis[curX][curY] + 1
            queue.append([nx,ny])
  

print(bfs(0,0))


