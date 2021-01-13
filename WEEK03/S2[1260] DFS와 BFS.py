import sys

def dfs(v,visited):
    visited[v] = 1 # 현재 노드를 방문 처리
    print(v, end =' ')
    for i in range(1,n+1): # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
        if visited[i] == 0 and board[v][i] == 1:
            dfs(i ,visited)

def bfs(v,visited):
    queue = [v] # 현재 정점 저장
    visited[v] = 1 # 현재 노드를 방문 처리
    while queue: # 큐가 빌 때까지 반복
        v = queue.pop(0) # 큐에서 하나의 원소를 뽑아 출력
        print(v, end=' ')
        for i in range(1,n+1): # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
            if visited[i] == 0 and board[v][i] == 1:
                queue.append(i)
                visited[i] = 1

visited_dfs = [0]*1005
visited_bfs = [0]*1005
# dfs(graph, 1, visited)

n, m, v = map(int,sys.stdin.readline().split())
board=[[0]*1005 for i in range(1005)]
for i in range(m):
    x, y = map(int,input().split())
    board[x][y] = board[y][x] = 1
dfs(v,visited_dfs)
print()
bfs(v,visited_bfs)
