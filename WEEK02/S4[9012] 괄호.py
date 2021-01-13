# 실패
# import sys

# def checkVPS(someList):
#     closeFlag = False
#     openFlag = False
#     closeCnt = 0
#     openCnt = 0
#     if someList[-1] == '(' or len(someList) % 2 != 0:
#         print('NO')
#         return
#     else:
#         for i in range(len(someList)-1,-1,-1):
#             if closeFlag:
#                 if openFlag:
#                     if openCnt == closeCnt:
#                         closeFlag = False
#                         openFlag = False
#                         continue
#                     else :
#                         print('NO')
#                         return
#             if someList[i] == ')':
#                 someList.pop()
#                 closeCnt += 1
#                 closeFlag = True
#             else:
#                 someList.pop()
#                 openCnt += 1
#                 openFlag = True
            
#             if len(someList) == 0:
#                 break

#         if openCnt == closeCnt:
#             print('YES')
#             return
#         else:
#             print('NO')
#             return

# testcase = int(sys.stdin.readline())

# for i in range(testcase):
#     checkString = list(input()) 
#     checkVPS(checkString)

# sys를 이용해서 list입력받으면 개행문자 ('\n') 까지 입력받기때문에 input을 써줌


# 2번째 방법, 괄호가 다를떄마다 +1 -1 해준다. 근데 그 값이 음수가 나오면 쌍이 안맞으므로 NO를 리턴한다. (맨처음에 ')'가 있다면 이는 VPS가아니고, sum도 음수가 되므로 NO를 리턴한다.
import sys

def checkVPS(someList):
    sum = 0
    for i in someList:
        if i == '(':
            sum += 1
        else:
            sum -= 1
        
        if sum < 0:
            print('NO')
            return
    if sum == 0:
        print('YES')
    else :
        print('NO')


testcase = int(sys.stdin.readline())

for i in range(testcase):
    checkString = list(input()) 
    checkVPS(checkString)


# 디버깅 코드
# for i in range(5,-1,-1):
#     print(i)

# import sys
# i = sys.stdin.readline()
# print(i)

# a= list('(())())')
# print(len(a))