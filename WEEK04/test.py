import sys
sys.setrecursionlimit(1000000)
debug = True
# if debug : sys.stdin = open('input.txt', 'r')
n, m = map(int, sys.stdin.readline().rstrip().split())
arr = [[0 for _ in range(m)] for _ in range(n)]
for idx in range(n) :
    arr[idx] = list(map(int, sys.stdin.readline().rstrip().split()))

dp = [[-1 for _ in range(m)] for _ in range(n)]

dp[0][0] = 1


dy=[-1, 1, 0, 0]
dx=[ 0, 0,-1, 1]
def rec(y, x) :
    if dp[y][x] == -1 :
        dp[y][x] = 0
        for idx in range(4) :
            _y = y + dy[idx]; _x = x + dx[idx]
            if _y < 0 or _y > n - 1 or _x < 0 or _x > m - 1 :
                continue
            if arr[_y][_x] > arr[y][x] :
                dp[y][x] += rec(_y,_x)
    if debug : print(f'rec :: ({y},{x}), dp[{y}][{x}] :: {dp[y][x]}')
    return dp[y][x]
print(rec(n-1,m-1))
if debug : print(dp)