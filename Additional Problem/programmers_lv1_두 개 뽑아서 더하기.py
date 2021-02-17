def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                answer.append(numbers[i] + numbers[j])
    answerSet = set(answer)
    newAnswer = list(answerSet)
    newAnswer.sort()

    return newAnswer

numbers = [5,0,2,7]
print(solution(numbers))


# # 다른 사람 풀이

# def solution(numbers):
#     answer = []
#     for i in range(len(numbers)):
#         for j in range(i+1, len(numbers)):
#             answer.append(numbers[i] + numbers[j])
#     return sorted(list(set(answer)))

# # 이게 좀더 깔끔한듯