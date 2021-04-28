import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
m, n = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(m)]
vis = [[-1 for _ in range(n)] for _ in range(m)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(curX, curY):
    print("curX = "+ str(curX) + ", curY = "+ str(curY))

    if curX == m-1 and curY == n-1: # 목표점에 도달했다면
        return 1
    if vis[curX][curY] == -1: # 한번도 방문하지 않았다면
        vis[curX][curY] = 0
        for dir in range(4):
            nx = curX + dx[dir]
            ny = curY + dy[dir]
            if nx < 0 or ny <0 or nx >= m or ny >= n:
                continue
            if board[curX][curY] > board[nx][ny]:
                vis[curX][curY] += dfs(nx, ny)
                # print("curX = "+ str(curX) + ", curY = "+ str(curY))
                # print(vis[curX][curY])

    return vis[curX][curY] 

print(dfs(0,0))



