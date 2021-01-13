n, k = map(int,input().split())

bag = [[] for _ in range(n+1)]

for i in range(1, n+1):
    bag[i] = list(map(int,input().split()))

dp = [[0 for _ in range(k+1)] for _ in range(len(bag)+1)]

for i in range(1,len(bag)+1):
    for j in range(1,k+1):
        if bag[i][0] <= j:
            