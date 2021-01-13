# 틀림
# t = int(input())


# cnt = 0
# result = []
# result_n=[]

# for _ in range(t):
#     n = int(input())
#     result_n.append(n)
#     score = [[] for _ in range(n)]
    
#     for i in range(n):
#         score[i] = list(map(int,input().split()))
    
#     for i in range(n-1):
#         if score[i][0] > score[i+1][0] and score[i][1] > score[i+1][1]:
#             cnt += 1
#         elif score[i][0] < score[i+1][0] and score[i][1] < score[i+1][1]:
#             cnt += 1
#         else: 
#             pass
#     result.append(cnt)

# for i in range(len(result)):
#     print(result_n[i] - result[i])
    
import sys
t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    rank = [[] for _ in range(n)]
    
    for i in range(n):
        rank[i] = list(map(int,sys.stdin.readline().split()))
    rank.sort()

    cnt = 1
    min = rank[0][1]

    for i in range(1, n):
        if rank[i][1] < min:
            min = rank[i][1]
            cnt += 1
    print(cnt)


