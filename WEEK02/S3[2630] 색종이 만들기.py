# # 1번째 방법 실패
# import sys
# num = int(sys.stdin.readline())
# board = [[int(x) for x in sys.stdin.readline().split()] for y in range(num)]
# board1 = [[ int(0) for _ in range(len(board))] for _ in range(len(board))]
# board2 = [[ int(0) for _ in range(len(board))] for _ in range(len(board))]
# board2 = [[ int(0) for _ in range(len(board))] for _ in range(len(board))]
# board2 = [[ int(0) for _ in range(len(board))] for _ in range(len(board))]



# cntWhite = 0
# cntBlue = 0

# def colorPaper(board):
#     global cntWhite
#     global cntBlue
#     global board1
#     global board2
#     global board3
#     global board4

#     if len(board1) == 1 and board1[0][0] == 0:
#         cntWhite += 1
#         return
#     elif len(board1) == 1 and board1[0][0] == 1:
#         cntBlue += 1
#         return

#     board1 = [ row[:len(board)//2] for row in board[0:len(board)//2] ]
#     board2 = [ row[len(board)//2:len(board)] for row in board[0:len(board)//2] ]
#     board3 = [ row[:len(board)//2] for row in board[len(board)//2:len(board)] ]
#     board4 = [ row[len(board)//2:len(board)] for row in board[len(board)//2:len(board)]]


#     chkCntBlue = 0
#     chkCntWhite = 0
#     for i in range(len(board1)):
#         for j in range(len(board1)):
#             if board1[i][j] == 1:
#                 chkCntBlue += 1
#             else:
#                 chkCntWhite += 1
#     if chkCntBlue == len(board1)*len(board1):
#         cntBlue += 1
#         return
#     elif chkCntWhite == len(board1)*len(board1):
#         cntWhite += 1
#         return
#     colorPaper(board1)

#     chkCntBlue = 0
#     chkCntWhite = 0
#     for i in range(len(board2)):
#         for j in range(len(board2)):
#             if board2[i][j] == 1:
#                 chkCntBlue += 1
#             else:
#                 chkCntWhite += 1
#     if chkCntBlue == len(board2)*len(board2):
#         cntBlue += 1
#         return
#     elif chkCntWhite == len(board2)*len(board2):
#         cntWhite += 1
#         return
#     colorPaper(board2)

#     chkCntBlue = 0
#     chkCntWhite = 0
#     for i in range(len(board3)):
#         for j in range(len(board3)):
#             if board3[i][j] == 1:
#                 chkCntBlue += 1
#             else:
#                 chkCntWhite += 1
#     if chkCntBlue == len(board3)*len(board3):
#         cntBlue += 1
#         return
#     elif chkCntWhite == len(board3)*len(board3):
#         cntWhite += 1
#         return
#     colorPaper(board3)

#     chkCntBlue = 0
#     chkCntWhite = 0
#     for i in range(len(board4)):
#         for j in range(len(board4)):
#             if board4[i][j] == 1:
#                 chkCntBlue += 1
#             else:
#                 chkCntWhite += 1
#     if chkCntBlue == len(board4)*len(board4):
#         cntBlue += 1
#         return
#     elif chkCntWhite == len(board4)*len(board4):
#         cntWhite += 1
#         return
#     colorPaper(board4)


# colorPaper(board)
# print(cntBlue)
# print(cntWhite)

# 2번째 방법

import sys

numBlue = 0
numWhite = 0

def colorPaper(x,y,n):
    global board, numBlue, numWhite
    color = board[x][y]
    flag = False

    for i in range(x,x+n):
        if flag:
            break
        
        for j in range(y,y+n):
            if board[i][j] != color:
                colorPaper(x, y, n//2) # 2 사분면
                colorPaper(x, y+n//2, n//2) # 1 사분면
                colorPaper(x+n//2, y, n//2) # 3 사분면
                colorPaper(x+n//2, y+n//2, n//2) # 4 사분면
                flag = True
                break

    if flag == False:
        if board[x][y] == 1:
            numBlue += 1 # 이거 왜 오류임?
        else:
            numWhite += 1 
                

n = int(sys.stdin.readline())
board = []


# board 입력받기
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

colorPaper(0,0,n)
print(numWhite)
print(numBlue)

