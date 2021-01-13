import sys
from collections import deque
# sys.stdin = open('input.txt', 'r')
n = int(sys.stdin.readline().rstrip())

apartments = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]      #아파트 행렬
visited = [[0]*n for _ in range(n)]
queue=deque()           #bfs 활용을 위한 덱 사용
# print(apartments)
ans=[]                  #답으로 활용할 아파트 단지 수 리스트

#(처음에 잘못 생각한? 부분 - 기존 문제처럼 풀려고 함)
# 아파트가 존재하는 스타트 지점 만들기
# for i in range(n):
#     for j in range(n):
#         if apartments[i][j] == 1:
#             queue.append([i,j])
# print(queue)

#좌/우/하/상
dc=[-1,1,0,0]
dr=[0,0,1,-1]

count = 1               #단지당 아파트 갯수 세기
danji = 0               #bfs를 실행할 때만, 그 횟수를 세어서 단지수를 확인
def bfs(x,y):
    global count, danji
    queue.append([x,y])
    danji+=1                                    #단지 갯수 세주기
    while queue:
        start_r, start_c = queue.popleft()
        visited[start_r][start_c] = 1
        #아이디어 핵심에 해당하는 아파트가 없는 곳을 만나면 바로 함수 끝내버리기
        if apartments[start_r][start_c] == 0:
            return
        for dir in range(4):                    #4방향 탐색
            start_nr = start_r + dr[dir]
            start_nc = start_c + dc[dir]
            if start_nr <0 or start_nr >= n or start_nc <0 or start_nc>=n:
                continue
            if visited[start_nr][start_nc] == 0 and apartments[start_nr][start_nc] == 1:
                count+=1                                        #아파트가 있는 곳을 만나면 +1
                apartments[start_nr][start_nc] = count          #기존 아파트 행렬을 활용
                queue.append([start_nr, start_nc])
                
    ans.append(count)                                           #bfs탐색을 끝낼 때마다 아파트 갯수에 해당하는 값을 모아줌(추후 오름차순 정리)
    count = 1

#아이디어 핵심으로, 방문한 적 없고 아파트가 있는 좌표에서만 bfs를 실행(bfs 함수 안에서도 아파트가 없는 좌표를 만나면 바로 함수 끝냄=return)
for i in range(n):
    for j in range(n):
        if apartments[i][j] and visited[i][j] == 0:
            bfs(i,j)

# for k in range(n):
#     print(apartments[k])

print(danji)
ans.sort()
for i in range(len(ans)):
    print(ans[i])

