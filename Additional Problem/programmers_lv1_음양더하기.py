def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i] == True:
            answer += absolutes[i]
        else:
            answer += absolutes[i] * -1
    return answer

absolutes = [4,7,12]
signs = [True,False,True]
print(solution(absolutes, signs))