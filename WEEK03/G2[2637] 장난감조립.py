import sys
from collections import deque

n = int(input())
m = int(input())

inDegree = [0] * 101
result = [0] * 101
graph = [[] for _ in range(n+1)]
valChk = [[0] * 101 for _ in range(101)] # if valChk[cur][prev] 이면 prev로 cur를 만들때, prev의 갯수를 의미하는 리스트임!

for _ in range(m):
    cur, prev, val = list(map(int,sys.stdin.readline().split())) # prev -> cur 꼴임! 그래서 cur의 차수를 늘려준다!
    graph[prev].append(cur)
    inDegree[cur] += 1
    valChk[cur][prev] = val 

queue = deque() # 차수가 0 인 노드를 저장할 큐 생성
for i in range(1, n+1):
    if inDegree[i] == 0:
        result[i] = 1 # 처음 반복문을 돌때 차수가 0인 노드는 기본부품이라는 의미로 1을 저장
        queue.append(i) 
    
for i in range(n): # 노드만큼 반복문 돌린다. ( i는 안쓰임 )
    cur = queue.popleft() # 기본부품중 하나를 cur에 pop해서 넣어줌
    for j in range(len(graph[cur])): # 그래프에 있는 현재 노드안에 들어있는 다음노드 길이만큼 반복한다.
        next = graph[cur][j] # 다음 노드를 graph에서 찾는다.
        inDegree[next] -= 1 # 다음 노드의 차수를 하나 제거해준다.
        if inDegree[next] == 0: # 다음 노드의 차수가 0이라면?
            for here in range(1, n+1): # 현재 노드를 탐색하기 위한 반복문을 돌린다 (인덱스 번호를 사용해야 하므로 1부터 n까지 반복함)
                if result[here] == 1: # 현재 노드가 기본 부품이면 무시한다.
                    continue
                mul = valChk[next][here] # 현재노드가 기본부품이 아니면 next를 만들기위한 here(중간부품)의 갯수를 일단 mul에 저장 (나중에 기본부품 갯수와 곱하기 위함)
                for there in range(1, n+1): # 그리고 다시 there을 노드 n만큼 돌려서 기본부품을 찾아준다.
                    if valChk[here][there] != 0: # here을 조립하는데 there이 존재한다면
                        if result[there] == 1: # 그리고 그 there이 기본 부품이라면
                            valChk[next][there] += (valChk[here][there] * mul) # here을 만들기 위한 there 갯수는 이미 처음에 for _ in range(m) 에서 입력받았으므로 거기다가 mul을 곱하면 총 부품갯수를 더할 수 있다.
            queue.append(next)

    
for i in range(1,n+1):
    if result[i] == 1:
        print(i,valChk[n][i])