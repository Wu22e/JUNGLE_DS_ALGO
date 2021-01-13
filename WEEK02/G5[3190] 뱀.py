# # 1번째 방법, 너무 어렵게 생각하는듯 코드길이가 자꾸길어짐
# # import sys

# # snakeQueue = []
# # n = int(sys.stdin.readline()) # 보드의 크기
# # board = [[0]*n for _ in range(n)]
# # snakeBoard = [[0]*n for _ in range(n)]
# # snakeBoard[0][0] = 1
# # k = int(sys.stdin.readline()) # 사과의 개수
# # for i in range(k):
# #     position = list(map(int,sys.stdin.readline().split()))
# #     board[position[0]-1][position[1]-1] = 1
# # l = int(sys.stdin.readline()) # 뱀의 방향 변환 횟수
# # for i in range(l):
# #     changeInfo = list(input().split())
# #     snakeQueue.append([changeInfo[0],changeInfo[1]]) # 이동길이 및 변환정보


# # cur = [0,0]
# # snakePosition=[[0,0]]
# # time = 0
# # while snakeQueue:

# #     if cur[0][0] == 0 and cur[0][1] == 0:
# #         for i in range(1, snakeQueue[0][0] + 1):
# #             if board[0][i] == 0:
# #                 snakePosition.append([cur[0][0], cur[0][1] + i])
# #                 snakePosition.pop(0)
# #             elif board[0][i] == 1:
# #                 snakePosition.append([cur[0][0], cur[0][1] + i])

# #             for j in range(len(snakePosition)):
# #                 if snakeBoard[snakePosition[j][0]][snakePosition[j[1]] != 1:
# #                     snakeBoard[snakePosition[j][0]][snakePosition[j][1]] = 1
# #                 elif snakeBoard[snakePosition[j][0]][snakePosition[j[1]] == 1:
# #                     print(time)
# #                     exit(0)
# #             time += 1
                    
# # 2번째 방법
            
import sys

# 상(0) 우(1) 하(2) 좌(3)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def changeDirection(direction,c):
    # 상(0) 하(2) 좌(4) 우(1)
    # 오른쪽 회전 : 상(0) -> 우(1) -> 하(2) -> 좌(3) -> 상(0) 
    # 왼쪽 회전   : 상(0) -> 좌(3) -> 하(2) -> 우(1) -> 상(0)
    if c =='L': # 왼쪽 회전
        direction = (direction-1)%4
    else:
        direction = (direction+1)%4
    return direction

snakePosition = []
snakeInfo = []
n = int(sys.stdin.readline()) # 보드의 크기
board = [[0]*n for _ in range(n)]
snakeBoard = [[0]*n for _ in range(n)]
snakeBoard[0][0] = 1
k = int(sys.stdin.readline()) # 사과의 개수
for i in range(k):
    position = list(map(int,sys.stdin.readline().split()))
    board[position[0]-1][position[1]-1] = 1
l = int(sys.stdin.readline()) # 뱀의 방향 변환 횟수
for i in range(l):
    length, direction= input().split()
    snakeInfo.append([int(length),direction]) # 이동길이 및 변환정보

time = 0 # 처음 시간
cur = [0, 0]
board[cur[0]][cur[1]] = -1
direction = 1
index = 0

snakePosition.append([0, 0])
while True:
    if index < len(snakeInfo):
        if snakeInfo[index][0] == time:
            direction = changeDirection(direction,snakeInfo[index][1])
            index += 1
    nx = cur[0] + dx[direction]
    ny = cur[1] + dy[direction]

    if (nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] == -1):
        time += 1
        break
    else:
        if board[nx][ny] == 1:
            board[nx][ny] = -1
            snakePosition.append([nx, ny])
        elif board[nx][ny] == 0:
            board[nx][ny] = -1
            snakePosition.append([nx, ny])
            tailX,tailY= snakePosition.pop(0)
            board[tailX][tailY] = 0
        cur[0] = nx
        cur[1] = ny
        time += 1

print(time)




