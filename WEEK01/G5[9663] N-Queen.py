# import math

# def nQueen(n):
#     board = [[1] * n for _ in range(n)]
#     for k in range(math.ceil(n/2)):
#         for i in range(n):
#             board[i][k] = 0
#             board[k][i] = 0
#             board[i][i+k] = 0 
board = [[1] * 5 for _ in range(5)]
for i in range(5):
    board[0][i] = 0
print(board)

# print(math.ceil(3/2))