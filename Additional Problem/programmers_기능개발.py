import math
import collections

def solution(progresses, speeds):
    answer = []
    day = collections.deque()
    for i in range(len(progresses)):
        day.append(math.ceil((100-progresses[i])/speeds[i]))
    print(day)
    while day :
        first = day.popleft()
        cnt = 1
        while day and first >= day[0] :
            cnt += 1
            day.popleft()
        answer.append(cnt)
    return answer
progresses = [95, 90, 99, 99, 80, 99]	
speeds = [1, 1, 1, 1, 1, 1]
print(solution(progresses, speeds))