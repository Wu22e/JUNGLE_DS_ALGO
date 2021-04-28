def solution(n, lost, reserve):
    answer = 0
    
    cnt = 0 # lost중 빌려서 체육수업을 들을 수 있는 학생 수
    
    save = []
    for i in range(len(lost)):
        if lost[i] in reserve:
            del reserve[reserve.index(lost[i])]
            save.append(i)
            
    for i in range(len(save)):
        del lost[save[i]]
    
    save2 = []
    
    for i in range(len(lost)):
        
        if lost[i]-1 <= 0:
            if lost[i]+1 in reserve:
                cnt += 1
                del reserve[reserve.index(lost[i]+1)]
                save2.append(i)
        elif lost[i]-1 > 0:
            if lost[i] + 1 <= n:
                if lost[i]+1 in reserve:
                    cnt += 1
                    del reserve[reserve.index(lost[i]+1)]
                    save2.append(i)
            
            elif lost[i] + 1 > n:
                if lost[i]-1 in reserve:
                    cnt += 1
                    del reserve[reserve.index(lost[i]-1)]
                    save2.append(i)
    # print("lost" + str(lost))
    # del lost[save2[0]]
    # print(lost)
    # print("save2" + str(save2))
    # num = len(save2)
    # print(num)
    # for i in range(num):
    #     del lost[save2[i]]
    

    answer += cnt + ( n - len(lost) - len(save2) ) 
    
    return answer

n = 5
lost = [2, 4]
reserve = [1,3,5]
print(solution(n, lost, reserve))