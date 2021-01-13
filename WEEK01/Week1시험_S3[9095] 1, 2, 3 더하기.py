# # 실패
testcase = int(input())

def sum123(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    return sum123(n-1) + sum123(n-2) + sum123(n-3)
for _ in range(testcase):
    print(sum123(int(input())))

# # 2번째 방법
# # from itertools import product
# #     for j in product()
# testcase = int(input())

# for i in range(testcase):
#     n = int(input())


