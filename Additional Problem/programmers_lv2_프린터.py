from collections import deque

def solution(priorities, location):
    answer = 0
    queueList = deque()
    for i, j in enumerate(priorities):
        queueList.append([j, i]) 
    
    while queueList:
        left = queueList.popleft()
        if queueList and left[0] < max(queueList)[0]: # 제일 큰놈이 아니면 뒤에 붙여줌
            queueList.append(left) 
        else: # 제일 큰놈이면 얘는 queueList에서 빠지게되면서 그 자리가 정해진다(answer로 자리를 표현)
            answer += 1
            if left[1] == location:
                break
            
    return answer


priorities = [1,1,9,1,1,1]
location = 0
print(solution(priorities, location))