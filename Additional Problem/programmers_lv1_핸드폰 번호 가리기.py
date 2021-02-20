def solution(phone_number):
    answer = ''
    for _ in range(len(phone_number)-4):
        answer = answer + '*'
    for i in range(4):
        answer = answer + phone_number[-4+i]
    return answer

# 태양이 형 코드
# def solution(phone_number):
#     phone_length = len(phone_number)
#     answer = ['*' for _ in range(phone_length - 4)]
#     answer.extend(phone_number[-4:])
#     return ''.join(answer)

phone_number = "01033334444"
print(solution(phone_number))