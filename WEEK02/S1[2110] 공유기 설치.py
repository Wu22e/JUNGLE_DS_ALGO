import sys
n,c = sys.stdin.readline().split()
n=int(n)
c=int(c)

homeList = []
for i in range(n):
    homeList.append(int(input()))

homeList.sort()

start = 1
end = homeList[-1] - homeList[0]


while start<=end:
    cnt = 1
    mid = (start + end) // 2
    prevHome = homeList[0]

    for i in range(1,len(homeList)):
        if homeList[i] - prevHome >= mid:
            cnt += 1
            prevHome = homeList[i]
    
    if cnt >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)
  
            


