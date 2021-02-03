import sys
input = sys.stdin.readline

def init(n):
    for i in range(1,n+1):
        parent[i] = i
        level[i] = 1

def find(u):
    if u == parent[u]:
        return u
    parent[u] = find(parent[u])
    return parent[u]

def merge(u, v):
    u = find(u)
    v = find(v)

    if u == v: return

    if level[u] > level[v]: u,v = v,u

    parent[u] = v

    if level[u] == level[v]:
        level[v] += 1


n, m = map(int, input().split())
parent = [0 for _ in range(n+1)]
level = [0 for _ in range(n+1)]
init(n)
for _ in range(m):
    mode, set1, set2 = map(int, input().split())
    if mode == 0:
        merge(set1, set2)

    elif mode == 1:
        if find(set1) == find(set2):
            print('YES')
        else:
            print('NO')