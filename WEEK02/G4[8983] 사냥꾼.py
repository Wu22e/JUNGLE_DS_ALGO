import sys

def isCatch(x,y,position,l):
    start = 0
    end = len(position) - 1
    while start <= end:
        mid = (start + end) // 2

        if position[mid] == x:
            if y <= l:
                return True
            else:
                return False
            
        elif position[mid] < x:
            if mid + 1 > len(position) - 1:
                if abs(position[mid] - x) + y <= l:
                    return True
                else:
                    return False
            if position[mid + 1] < x:
                start = mid + 1
            elif abs(position[mid] - x) <= abs(position[mid+1] - x):
                if abs(position[mid] - x) + y <= l:
                    return True
                else:
                    return False
            elif abs(position[mid] - x) >= abs(position[mid+1] - x):
                if abs(position[mid+1] - x) + y <= l:
                    return True
                else:
                    return False

        elif position[mid] > x:
            if mid - 1 < 0:
                if abs(position[mid] - x) + y <= l:
                    return True
                else:
                    return False
            if position[mid - 1] > x:
                end = mid - 1
            elif abs(position[mid] - x) <= abs(position[mid-1] - x):
                if abs(position[mid] - x) + y <= l:
                    return True
                else:
                    return False
            elif abs(position[mid] - x) >= abs(position[mid-1] - x):
                if abs(position[mid-1] - x) + y <= l:
                    return True
                else:
                    return False
    return False




m,n,l= map(int,sys.stdin.readline().split())
position = list(map(int,sys.stdin.readline().split()))

position.sort()
cnt = 0
for i in range(n):
    x,y = map(int, sys.stdin.readline().split())
    if isCatch(x,y,position,l):
        cnt += 1

print(cnt)
