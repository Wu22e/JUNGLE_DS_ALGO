import sys,itertools

n = int ( sys.stdin.readline())
a =list(map(int,sys.stdin.readline().split())) 

sum = 0
sumList = []
for perm in itertools.permutations(a):
    for i in range(len(perm)-1):
        sum = sum + abs(perm[i]-perm[i+1])
    sumList.append(sum)
    sum = 0
print(max(sumList))