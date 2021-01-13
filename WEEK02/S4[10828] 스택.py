# 1번째 방법 : 시간초과
import sys
stack = []

commandNum = int(sys.stdin.readline())
commandList = []
for i in range(commandNum):
    commandList = sys.stdin.readline().split()
    if commandList[0] == 'push':
        stack.append(commandList[1])
    elif commandList[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop(-1)
    elif commandList[0] == 'size':
        print(len(stack))
    elif commandList[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else :
            print(0)
    elif commandList[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    else :
        pass

# 2번째 방법

# stack = [0] * 10001

# commandNum = int(input())
# commandList = []
# for i in range(commandNum):
#     commandList = input().split()
#     if commandList[0] == 'push':
#         stack.append(commandList[1])
#         stack[i] = commandList[1]
#     elif commandList[0] == 'pop':
#         if len(stack) == 0:
#             print(-1)
#         else:
#             print(stack[-1])
#             stack.pop(-1)
#     elif commandList[0] == 'size':
#         print(len(stack))
#     elif commandList[0] == 'empty':
#         if len(stack) == 0:
#             print(1)
#         else :
#             print(0)
#     elif commandList[0] == 'top':
#         if len(stack) == 0:
#             print(-1)
#         else:
#             print(stack[-1])
#     else :
#         pass

# # 디버깅 코드
# k=[]
# k = input().split()
# print(k)
# a = [1, 2, 3]
# a.pop(-1)
# print(a)