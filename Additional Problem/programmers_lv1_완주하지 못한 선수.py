# 시간 초과
# def solution(participant, completion):
#     for i in completion:
#         if i in participant:
#             participant.remove(i)
#     return participant[0]

def solution(participant, completion):
    answer = {}
    for i in participant:
        if i not in answer:
            answer[i] = 1
        else:
            answer[i] += 1
    for i in completion:
        answer[i] -= 1
    
    for key, value in answer.items():
        if value == 1:
            return key


participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

print(solution(participant, completion))
