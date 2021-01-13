import sys

n = int(sys.stdin.readline())
board = [[0]*n for _ in range(n)]

appleNum = int(sys.stdin.readline())
for i in range(appleNum):
    position = list(map(int, sys.stdin.readline().split()))
    board[position[0]-1][position[1]-1] = 1

dirChangeNum = int(sys.stdin.readline())
for i in range(dirChangeNum):
    info = list(map(str, sys.stdin.readline().split()))

print(info)