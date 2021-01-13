# 투포인터 이용 (근데 왜틀렸지? 모르겠음)

# import sys

# n = int(sys.stdin.readline())
# solProperty = list(map(int,sys.stdin.readline().split()))

# solProperty.sort()

# start = 0
# end = n - 1
# sum = 0
# compareValue = []
# indexStack = []
# while start < end:
#     sum = solProperty[start] + solProperty[end]
#     compareValue.append(sum)
#     indexStack.append([start,end])
#     if len(compareValue) == 2:
#         if abs(compareValue[0]) < abs(compareValue[1]):
#             compareValue.pop(1)
#             indexStack.pop(1)
#         else:
#             compareValue.pop(0) 
#             indexStack.pop(1)

#     if sum == 0:
#         print(solProperty[start],solProperty[end])
#     elif sum < 0:
#         start += 1
#     elif sum > 0:
#         end -= 1

# print(solProperty[indexStack[0][0]],solProperty[indexStack[0][1]])

# 다시 풀기

import sys

n = int(sys.stdin.readline())
solProperty = list(map(int,sys.stdin.readline().split()))

solProperty.sort()

start = 0
end = n - 1
sum = solProperty[start] + solProperty[end]
left = start
right = end

while start < end:
    tempSum = solProperty[start] + solProperty[end]
    if abs(tempSum) < abs(sum):
        sum = tempSum
        left = start
        right = end
        if tempSum == 0:
            break

    if tempSum < 0:
        start += 1
    else:
        end -= 1

print(solProperty[left],solProperty[right])

