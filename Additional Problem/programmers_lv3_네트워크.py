from collections import deque
def solution(n, computers):
    answer = 0
    vis = [False for _ in range(n)]
    for i in range(n):
        if vis[i] == False:
            # vis[i] = True
            queue = deque()
            queue.append(i)
            while queue:
                start = queue.popleft()
                vis[start] = True
                for j in range(n):
                    if j != start and computers[start][j] == 1:
                        if vis[j] == False:
                            queue.append(j)
            answer += 1
    return answer

n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

print(solution(n, computers))
