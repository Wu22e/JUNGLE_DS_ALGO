def solution(numbers, target):
    sup = [0]
    for i in numbers:
        sub = []
        for j in sup:
            sub.append(j+i)
            sub.append(j-i)
        sup = sub

    return sub.count(target)


numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))