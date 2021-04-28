
from collections import deque

def solution(enter, leave):
    # answer = []
    # return answer
    result = [0 for _ in range(len(enter))]
    # print(result)
    dq = deque()
    # print(len(dq))
    index = 0
    cnt = 0
    for i in range(len(enter)):
        dq.append(enter[i])
        for j in range(len(leave)):
           
            # if (cnt != len(enter)) and (index != len(enter)) and (leave[index] == dq[cnt]):
            if leave[i] == dq[j]:
                for k in range(cnt+1):
                    result[k] += len(dq) - 1
                dq.pop()
                index += 1

    print(dq)
    print(result)


enter = [1,4,2,3]
leave = [2,1,3,4]
# result = [2,2,1,3]

solution(enter,leave)

# dq = deque()
# dq.append(1)
# dq.append(2)
# print(dq[1])








# enter	leave	result
# [1,3,2]	[1,2,3]	[0,1,1]
# [1,4,2,3]	[2,1,3,4]	[2,2,1,3]
# [3,2,1]	[2,1,3]	[1,1,2]
# [3,2,1]	[1,3,2]	[2,2,2]
# [1,4,2,3]	[2,1,4,3]	[2,2,0,2]