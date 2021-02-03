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

    if cost[u] > cost[v]:
        parent[u] = v
    else:
        parent[v] = u

    if level[u] == level[v]:
        level[v] += 1

n, m, k = map(int, input().split())

parent = [0 for _ in range(n + 1)]
level = [0 for _ in range(n + 1)]

init(n)

cost = list(map(int,input().split()))
cost.insert(0,0)

for _ in range(m):
    v, w = map(int, input().split())
    if find(v) != find(w):
        merge(find(v), find(w))

lowest_cost = 0

for i in range(1, n+1):
    if find(i) != 0:
        lowest_cost += cost[find(i)]
        merge(0, find(i))

if lowest_cost > k:
    print("Oh no")
else:
    print(lowest_cost)
