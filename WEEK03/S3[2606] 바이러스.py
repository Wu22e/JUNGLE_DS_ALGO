def bfs(v,visited):
    cnt=0
    queue=[v]
    visited[v] = 1
    while queue:
        v = queue.pop(0)
        for i in range(1,num+1):
            if visited[i] == 0 and board[v][i] == 1:
                queue.append(i)
                visited[i] = 1
                cnt += 1
    return cnt

visited= [0]*105

num = int(input())
connectNum = int(input())
board = [[0] * 105 for _ in range(105)]
for i in range(connectNum):
    x, y = map(int,input().split())
    board[x][y] = board[y][x] = 1

print(bfs(1,visited))

