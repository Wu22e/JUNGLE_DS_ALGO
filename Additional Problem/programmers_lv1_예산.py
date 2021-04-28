def solution(d, budget):
    coinSum = 0
    cnt = 0
    d.sort()
    for i in range(len(d)):
        coinSum += d[i]
        if coinSum > budget:
            break
        cnt += 1
    

    return cnt

d = [2,2,3,3]
budget = 10
print(solution(d, budget))