day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
endDay = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def solution(a, b):
    answer = ''
    dayCnt = 0 
    for i in range(1, a+1):
        if i == a:
            dayCnt += b-1
            break
        dayCnt += endDay[i]
    answer = day[dayCnt%7]
    return answer

a = 5
b = 24
# result = 'TUE'
print(solution(a,b))