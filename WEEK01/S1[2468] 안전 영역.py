
import sys

n = int ( sys.stdin.readline())
board = [[int(x) for x in sys.stdin.readline().split()] for y in range(n)]
newBoard = [[1] * n for _ in range(n)]
vis = [[0] * n for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
cur = [0, 0]
safeZoneNum = 0
safeZoneNumList = []

for rainAmount in range(max(max(board))+1):  # 이중리스트에서 가장 큰값을 뽑는방법으로 이렇게 해도 되는가??
    if rainAmount == 0:
        safeZoneNum = 1
    elif rainAmount == max(max(board)):
        safeZoneNum = 0
    else:
        for i in range(n):
            for j in range(n):
                if board[i][j] <= rainAmount:
                    newBoard[i][j] = 0

        for i in range(n):
            for j in range(n):
                if (newBoard[i][j] == 0 or vis[i][j]) :
                    continue

                Q = []
                vis[i][j] = 1
                Q.append([i, j])

                while len(Q) != 0:
                    cur = Q[0]
                    Q.pop(0) # front pop
                    for dir in range(4):
                        nx = cur[0] + dx[dir]
                        ny = cur[1] + dy[dir]
                        if (nx < 0 or nx >= n or ny < 0 or ny >= n):
                            continue
                        if (vis[nx][ny] or newBoard[nx][ny] != 1):
                            continue
                        vis[nx][ny] = 1
                        Q.append([nx, ny])
                safeZoneNum += 1
    safeZoneNumList.append(safeZoneNum)
    safeZoneNum = 0
    newBoard = [[1] * n for _ in range(n)]
    vis = [[0] * n for _ in range(n)]

print(max(safeZoneNumList))



