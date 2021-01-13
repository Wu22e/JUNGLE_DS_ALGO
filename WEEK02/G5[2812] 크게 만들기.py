n, k=input().split()
n=int(n)
k=int(k)

numList = list(input())
numStack = []
tk=k # 왜 새로운 값을 할당해야 하지?
for i in range(n):
    while tk > 0 and numStack and numStack[-1] < numList[i]:
            numStack.pop()
            tk -= 1
    numStack.append(numList[i])
print(''.join(numStack[:n-k]))








# print(numStack)


# for _ in range(k):
#     numStack.append(numList.pop(0))

# while len(numStack) == k:
#     for i in range(k-1)
#         if numStack[i] < numStack[i+1]:
#             numStack.pop(i)
#         else:
#             break

#         if len(numStack) == k-1:
#             numStack.append(numList.pop(0))



# while numList:
#     numStack.append(numList.pop(0))
#     if numStack[1] < numStack[2]:
#         numStack.pop(1)
#     else:
#         numStack.pop(2)

# print(numStack[0] + numStack[1])