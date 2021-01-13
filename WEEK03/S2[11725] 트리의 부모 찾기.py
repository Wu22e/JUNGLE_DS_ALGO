import sys

def dfs1(graph, v, visited):
    visited[v] = True 
    # print(v, end =' ')
    for i in graph[v]:
        if visited[i] == False :
            result[i] = v
            dfs1(graph, i, visited)

def dfs2(graph, v, visited):
    queue = [v] 
    visited[v] = True 
    while queue: 
        v = queue.pop() 
        # print(v, end=' ')
        for i in graph[v]: 
            if visited[i] == False :
                queue.append(i)
                visited[i] = 1
                result[i] = v

n = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n+1)]
visited = [False] * (100005)
result = [0] * (100005)

for _ in range(n-1):
    x, y = list(map(int,input().split()))
    # print(x,y)
    graph[x].append(y)
    graph[y].append(x)
    
dfs2(graph, 1, visited)
for i in range(2,n+1):
    print(result[i])


