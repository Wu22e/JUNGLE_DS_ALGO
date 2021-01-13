value = 0
def checkVPS(someList):
    checkStack = []
    global value
    for i in someList:
        if i == '(' or i == '[':
            checkStack.append(i)
        elif i == ')':
            temp = 0
            while checkStack:
                top = checkStack.pop()
                if top == '(':
                    if temp == 0:
                        checkStack.append(2)
                    else:
                        checkStack.append(2*temp)
                    break
                elif top == '[':
                    print(0)
                    exit(0)
                else:
                    temp = temp + int(top)
        elif i == ']':
            temp = 0
            while checkStack:
                top = checkStack.pop()
                if top == '[':
                    if temp == 0:
                        checkStack.append(3)
                    else:
                        checkStack.append(3*temp)
                    break
                elif top == '(':
                    print(0)
                    exit(0)
                else:
                    temp = temp + int(top)
    
    for i in checkStack:
        if i == '(' or i == '[':
            print(0)
            exit(0)
        else:
            value += i


checkString = list(input()) 
checkVPS(checkString)
print(value)


# 또 다른 신박한 방법
# import sys
# string = sys.stdin.readline().strip()
# stack = []
# multi = 1
# answer = 0
# pre = ''
# pair = {')': '(', ']': '['}
# score = {'(': 2, '[': 3}
# for s in string:
#     if s in '([':
#         stack.append(s)
#         # 여는 괄호가 중첩될 때마다 해당 괄호가 닫힐 때 더해질 값을 미리 곱함
#         multi *= score[s]
#     elif stack:
#         if stack[-1] == pair[s]:
#             stack.pop()
#             # 이전의 문자열이 현재 닫는 괄호와 쌍을 이루는 여는 괄호 인 경우에만 값을 추가
#             # 그 외에는 닫는 괄호는 이미 그 전에 저장된 값의 곱으로 반영되어 있음
#             if pre == pair[s]:
#                 answer += multi
#             # 괄호가 닫혔으니 해당 괄호 만큼 곱했던 값을 나누어 줌
#             multi //= score[pair[s]]
#         # 괄호끼리 쌍이 맞지 않으면 틀린 괄호
#         else:
#             answer = 0
#             break
#     # 여는 괄호가 없는데 닫히면 틀린 괄호
#     else:
#         answer = 0
#         break
#     # 괄호가 닫힐 때 현재 값을 저장할 지 판단하기 위해 직전 문자를 저장
#     pre = s
# # 스택에 값이 남으면 틀린 괄호.
# if stack:
#     answer = 0
# print(answer)
