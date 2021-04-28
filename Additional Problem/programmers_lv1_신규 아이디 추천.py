def solution(new_id):
    # step 1
    new_id = new_id.lower()
    # print("1단계 : " + new_id)
    # step 2
    temp = ''
    for i in new_id:
        if i.isalnum() or  i in "-_.":
            temp += i
    
    answer = temp
    # print("2단계 : " + answer)
    # step 3
    temp = ''
    cnt = 0
    for i in answer:
        if i == '.':
            cnt += 1
        else:
            cnt = 0
        
        if cnt >= 2:
            continue

        temp += i
    answer = temp
    # print("3단계 : " + answer)

    # step 4
    if answer[0] == '.' and answer[-1] == '.':
        answer = answer[1:-1]
    elif answer[0] == '.' and answer[-1] != '.':
        answer = answer[1:]
    elif answer[0] != '.' and answer[-1] == '.':     
        answer = answer[:-1]

    # print("4단계 : " + answer)

    # step 5
    if len(answer) == 0:
        answer += 'a'
    
    # print("5단계 : " + answer)

    # step 6
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # print("6단계 : " + answer)

    # step 7
    if len(answer) <= 2:
        while(len(answer)<=2):
            answer += answer[-1]

    # print("7단계 : " + answer)


    return answer


new_id = "abcdefghijklmn.p"

# print(new_id)
print(solution(new_id))