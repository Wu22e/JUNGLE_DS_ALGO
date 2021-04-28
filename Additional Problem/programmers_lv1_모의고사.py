rule1 = [1,2,3,4,5]
rule2 = [2,1,2,3,2,4,2,5]
rule3 = [3,3,1,1,2,2,4,4,5,5]

def solution(answers):
    answer = []
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0

    for i in range(len(answers)):
        if(answers[i] == rule1[i%len(rule1)]):
            cnt1 += 1
        if(answers[i] == rule2[i%len(rule2)]):
            cnt2 += 1
        if(answers[i] == rule3[i%len(rule3)]):
            cnt3 += 1
    
    result = [cnt1, cnt2, cnt3]

    for person, score in enumerate(result):
        if score == max(result):
            answer.append(person+1)
    return answer
    


answers = [1,3,2,4,2]	
print(solution(answers))