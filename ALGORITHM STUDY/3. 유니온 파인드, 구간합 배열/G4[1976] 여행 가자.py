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

n = int(input())
m = int(input())

parent = [0 for _ in range(n + 1)]
level = [0 for _ in range(n + 1)]
init(n)

for i in range(n):
    isTrue = list(map(int,input().split()))
    for j in range(n):
        if j > i and isTrue[j] == 1:
            merge(i, j)
flag = False
city = list(map(int,input().split()))

for i in range(len(city)-1):
    if find(city[i]-1) == find(city[i+1]-1):
        flag = True
    else:
        flag = False
        break
if flag:
    print('YES')
else:
    print('NO')


