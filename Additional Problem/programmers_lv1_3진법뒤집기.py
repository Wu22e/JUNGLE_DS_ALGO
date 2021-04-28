def solution(n):
    answer = ''
    if n < 3:
        return n
    while True:
        answer += str(n%3)
        n = n // 3
        if n < 3:
            answer += str(n)
            break
    decimal = 0

    for i in range(len(answer)-1,-1,-1):
        decimal += int(answer[i])*(3**(len(answer)-1-i))
    return decimal

n = 4
print(solution(n))