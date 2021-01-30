# 이코드는 왜 안되는거지? ;;
# import sys
#
# input = sys.stdin.readline
#
#
# def recur_z(size,row,col):
#     global cnt
#     if size == 2:
#         if row == r and col == c:
#             print(cnt)
#             return
#         cnt += 1
#         if row == r and col + 1 == c:
#             print(cnt)
#             return
#         cnt += 1
#         if row + 1 == r and col == c:
#             print(cnt)
#             return
#         cnt += 1
#         if row + 1 == r and col + 1 == c:
#             print(cnt)
#             return
#         cnt += 1
#     else:
#         recur_z(size // 2, row, col)
#         recur_z(size // 2, row, col + size // 2)
#         recur_z(size // 2, row + size // 2, col)
#         recur_z(size // 2, row + size // 2, col + size // 2)
#
# N, r, c = map(int, input().split())
# cnt = 0
# recur_z(2**N, 0, 0)

import sys

input = sys.stdin.readline

N, r, c = map(int,input().split())

def recur_z(N,r,c):
    if N == 0: return 0
    half = (2 ** N) // 2

    if r < half and c < half:
        return recur_z(N-1, r, c)
    elif r < half and c >= half:
        return half*half + recur_z(N - 1, r, c - half)
    elif r >= half and c < half:
        return 2*half*half + recur_z(N - 1, r - half, c)
    else:
        return 3*half*half +recur_z(N - 1, r - half, c - half)

print(recur_z(N, r, c))
