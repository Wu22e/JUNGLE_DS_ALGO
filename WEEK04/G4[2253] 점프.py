import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
visit = [0] * (N+1)

for _ in range(M):
    visit[int(sys.stdin.readline())] = -1

que = deque()
que.append((2, 1))
visit[2] = 1
jump = 1

while que:
    len_que = len(que)

    for _ in range(len_que):
        pos, jump = que.popleft()
        jumps = (jump + 1, jump, jump - 1)

        for j in jumps:
            if j > 0:
                next_pos = pos + j
                if next_pos == N:
                    print(visit[pos] + 1)
                    exit()
                if next_pos <= N and visit[next_pos] != -1:
                    que.append((next_pos, j))
                    visit[next_pos] = visit[pos] + 1
                    
print(visit)