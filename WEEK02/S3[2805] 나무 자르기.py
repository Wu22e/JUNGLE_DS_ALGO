# 실패 (선형탐색이랑 다를 게 없는 풀이였음)
# import sys

# tree = list(map(int, sys.stdin.readline().split()))

# treeHeight = list(map(int, sys.stdin.readline().split()))

# midHeight = (min(treeHeight) + max(treeHeight)) // 2


# upFlag = False
# downFlag = False

# while True:
#     treeSum = 0
#     if upFlag == True and downFlag == True:
#         break
#     for i in range(tree[0]):
#         if treeHeight[i] - midHeight >= 0:
#             treeSum += treeHeight[i] - midHeight
#         else:
#             pass
#     if treeSum == tree[1]:
#         print(midHeight)
#         break
#     elif treeSum < tree[1]:
#         midHeight -= 1
#         upflag = True
#     else:
#         midHeight += 1
#         downFlag = True


# 2 번째 방법
import sys

tree = list(map(int, sys.stdin.readline().split()))

treeHeight = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(treeHeight)
result = 0

while start <= end:
    treeSum = 0
    midHeight = (start + end) // 2

    for i in range(tree[0]):
        if treeHeight[i] - midHeight > 0:
            treeSum += treeHeight[i] - midHeight

    if treeSum >= tree[1]:
        result = midHeight
        start = midHeight + 1
    elif treeSum < tree[1]:
        end = midHeight - 1

    
print(result)