# 1번째 방법 시간 초과  탑을 오른쪽에서 봤음( 완전 탐색 구현임 )
# import sys
# testcase = int(sys.stdin.readline())

# towerHeight = list(map(int,sys.stdin.readline().split()))

# receive = []

# for i in range(testcase):
#     if len(towerHeight) - 1 - i == 0:
#             receive.append(0)
#             break
#     for j in range(testcase):
#         if len(towerHeight) - 1 - j - i < 0:
#             receive.append(0)
#             break
#         elif towerHeight[len(towerHeight) - 1 - i] < towerHeight[len(towerHeight) - 1 - j - i]:
#             receive.append(len(towerHeight) - j - i)
#             break

# receive.reverse()

# for i in range(len(receive)):
#     print(receive[i],end=' ')

# 2번째 방법
import sys
n = int(sys.stdin.readline())
towerHeight = list(map(int,sys.stdin.readline().split()))
towerStack = []
answer = []

for i in range(n):
    while towerStack:
        if towerStack[-1][1] > towerHeight[i]: # 수신 가능한 상황
            answer.append(towerStack[-1][0] + 1)
            break
        else:
            towerStack.pop()
    if not towerStack:
        answer.append(0)    
    towerStack.append([i, towerHeight[i]])

for i in range(len(answer)):
    print(answer[i],end=' ')
# print(' '.join(map(str, answer)))


    
    

