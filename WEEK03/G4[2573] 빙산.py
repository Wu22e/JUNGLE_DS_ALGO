# 첫번 째 방법 시간초과 (딥카피, 배열이 너무많은듯)
# import sys, copy
# from collections import deque

# r, c = map(int,sys.stdin.readline().split())
# board = [list(map(int,sys.stdin.readline().split())) for _ in range(r)]
# newBoard = copy.deepcopy(board)
# vis =[[0]*c for _ in range(r)]

# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]

# Q = deque()

# def bfs():
#     global board,vis
#     year = 0
#     while True:
#         block = 0
#         for i in range(r):
#             for j in range(c):
#                 if board[i][j] == 0 or vis[i][j] != 0:    
#                     continue
#                 if block == 1:
#                     return year

#                 curX, curY = i, j
#                 Q.append([curX,curY])
#                 vis[curX][curY] = 1
#                 while Q:
#                     curX, curY = Q.popleft()
#                     for dir in range(4):
#                         nx = curX + dx[dir]
#                         ny = curY + dy[dir]
#                         if nx < 0 or nx >= r or ny < 0 or ny >= c:
#                             continue
#                         if vis[nx][ny] != 0:
#                             continue
#                         if board[nx][ny] == 0:
#                             if newBoard[curX][curY] == 0:
#                                 pass
#                             else:
#                                 newBoard[curX][curY] -= 1
#                             continue
#                         vis[nx][ny] = 1
#                         Q.append([nx,ny])
#                 block += 1
#         year += 1
#         vis =[[0]*c for _ in range(r)]
#         board = copy.deepcopy(newBoard)


# print(bfs())

# 2번째 방법   

import sys
from collections import deque

r, c = map(int,sys.stdin.readline().split())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(r)]
vis =[[0]*c for _ in range(r)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

Q = deque()

def bfs():
    global board,vis
    melt_info = []
    year = 0
    while True:
        block = 0
        for i in range(r):
            for j in range(c):
                if board[i][j] == 0 or vis[i][j] != 0:
                    continue
                if block == 1:
                    return year

                curX, curY = i, j
                Q.append([curX,curY])
                vis[curX][curY] = 1
                while Q:
                    cnt = 0
                    curX, curY = Q.popleft()
                    for dir in range(4):
                        nx = curX + dx[dir]
                        ny = curY + dy[dir]
                        # if nx < 0 or nx >= r or ny < 0 or ny >= c:
                        #     continue
                        if vis[nx][ny] != 0:
                            continue
                        if board[nx][ny] == 0:
                            cnt += 1
                            continue
                        vis[nx][ny] = 1
                        Q.append([nx,ny])     
                    melt_info.append([curX, curY, cnt])
                block += 1
        year += 1
        vis =[[0]*c for _ in range(r)]
        for i in range(len(melt_info)):
            board[melt_info[i][0]][melt_info[i][1]] -= melt_info[i][2]
            if board[melt_info[i][0]][melt_info[i][1]] < 0:
                board[melt_info[i][0]][melt_info[i][1]] = 0
        melt_info = [] # 이거 초기화 안해줘서 계속삑났음;;
        if block == 1:
            chkCnt = 0
            for i in range(r):
                for j in range(c):
                    if board[i][j] == 0:
                        chkCnt += 1
            if chkCnt == r*c:
                return 0

print(bfs())



    

