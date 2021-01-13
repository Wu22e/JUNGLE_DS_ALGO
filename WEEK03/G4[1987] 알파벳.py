import sys
from collections import deque
r, c = map(int,sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(r)]


Q = deque()
remember=[]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

maxVal = 1
def dfs(x,y,word):
    global maxVal
    curX = x
    curY = y
    curWord = word
    Q.append([curX, curY, curWord])
    while Q:
        curX, curY, curWord = Q.pop()
        for dir in range(4):
            nx = curX + dx[dir]
            ny = curY + dy[dir]
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            if board[nx][ny] in curWord:
                continue
            maxVal = max(maxVal,len(curWord+board[nx][ny]))
            Q.append([nx, ny, curWord + board[nx][ny]])

dfs(0,0,board[0][0])
# print(vis)
print(maxVal)
