import sys
from collections import deque
n, m = map(int,sys.stdin.readline().split())

inDegree = [0] * 32005
result = [0] * 32005
graph = [[] for _ in range(n+1)]

def topologySort():
    queue = deque()
    # 진입 차수가 0 인 노드를 큐에 삽입
    for i in range(1, n+1):
        if inDegree[i] == 0:
            queue.append(i)
    # 위상 정렬이 완전히 수행 되려면 정확히 N개의 노드를 방문한다
    for i in range(1, n+1):
        # n개를 방문하기 전에 큐가 빈다면 사이클이 발생한 것임
        if not queue:
            return
        x = queue.popleft() # 큐에 저장된 노드를 x에 저장
        result[i] = x # 결과값에 노드를 순서대로 저장
        for j in range(len(graph[x])):
            y = graph[x][j]
            inDegree[y] -= 1 # 새롭게 진입 차수가 0 이 된 정점을 큐에 삽입
            if inDegree[y] == 0:
                queue.append(y)
    for i in range(1,n+1):
        print(result[i])

for _ in range(m):
    x, y = list(map(int,input().split()))
    graph[x].append(y)
    inDegree[y] += 1
    # graph[y].append(x) # 얘 쓰게되면 그냥 dfs지 위상정렬이 아님
    
topologySort()