import sys
input = sys.stdin.readline
n, k = map(int, input().split())

appliance = list(map(int,input().split()))
history = [[] for _ in range(n)]:

plugin = [0] * n

for i in range(n):
    plugin[i] = appliance[i]

flag = False
cnt = 0

for i in range(k):
    for j in range(n):
        if n + i >= k:
            continue
        if plugin[j] in appliance[n+i:]:
            continue
        else:
            for s in range(n):
                if plugin[s] == appliance[n+i]:
                    flag = True
                    continue
            if flag:
                flag = False
                continue
            plugin[j] = appliance[n+i]
            cnt += 1

print(cnt)
    





