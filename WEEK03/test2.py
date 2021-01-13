import sys
from collections import deque

n, k = map(int,sys.stdin.readline().split())

vis = [0] * 100001
queue = deque([n])


dir = [1, -1]

def dfs():
    if n == k:
        print(0)
        return
    while queue:
        cur = queue.popleft()
        for i in range(3):
            if i <=1:
                next = cur + dir[i]
            else:
                next = cur * 2

            if next < 0 or next > 100000:
                continue

            if vis[next] != 0: 
                continue
            
            vis[next] = vis[cur] + 1
            if next == k:
                return
            else:
                queue.append(next)

dfs()
if n != k:
    print(vis[k])