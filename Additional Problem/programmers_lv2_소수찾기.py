from itertools import permutations

def isPrime(n):
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n%i == 0:
            return False
        i += 1
    return True

def solution(numbers):
    answer = 0
    comp = []
    for i in range(len(numbers)):
        combList = list(permutations(numbers,i+1))
        for j in range(len(combList)):
            temp = int(''.join(combList[j]))
            if temp in comp:
                continue
            comp.append(temp)
            if isPrime(temp):
                answer += 1

    return answer

numbers = "011"
print(solution(numbers))