def solution(arr):
    answer = []
    cnt = 1
    prev = arr[0]
    for i in range(1, len(arr)):
        if arr[i] != prev:
            answer.append(prev)
        prev = arr[i]
    if arr[-1] == prev:
        answer.append(prev)
    return answer
            
arr = [4,4,4,3,3]
print(solution(arr))