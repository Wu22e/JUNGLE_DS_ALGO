import sys,itertools

W = []
city = []
n = int ( sys.stdin.readline())
for i in range(n):
    city.append(i)

W = [[int(x) for x in sys.stdin.readline().split()] for y in range(n)]

index = []
_sum = 0
minCost = []

flag = False

for perm in itertools.permutations(city):
    # print(perm)
    for i in range(n-1):
        if W[perm[i]][perm[i+1]] == 0:
            flag = True
            break
    if flag:
        flag = False
        continue
    
    if W[perm[-1]][perm[0]] == 0:
        continue
    
            
    
    list_perm = list(perm)
    # print(list_perm)
    list_perm.append(list_perm[0])
    
    # print(list_perm)
    for i in range(len(list_perm)-1):
        _sum += W[list_perm[i]][list_perm[i+1]]
    # _sum += W[list_perm[len(list_perm)-1]][list_perm[0]]
    minCost.append(_sum)
    _sum = 0
# print(minCost)
print(min(minCost))


# 디버깅 코드 (리스트 인덱스 오버플로우 확인)

# a = [1, 2, 3, 4]
# print(a[4])

# 범위 벗어나면 안됨