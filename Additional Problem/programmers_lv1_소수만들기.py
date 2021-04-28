from itertools import combinations

def isPrime(n):
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if(n%i == 0):
            return False
        i += 1
    return True


def solution(nums):
    answer = 0
    combList = list(combinations(nums, 3))
    for i in range(len(combList)):
        if isPrime(sum(combList[i])):
            answer += 1
    return answer

nums = [1,2,7,6,4]

print(solution(nums))