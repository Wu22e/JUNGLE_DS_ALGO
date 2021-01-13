import sys

def binary_search(element, some_list):
    start = 0
    end = len(some_list)-1
    while start<=end:
        mid =(start + end)//2
        if some_list[mid] == element:
            return 1
        elif some_list[mid] > element:
            end = mid - 1
        else:
            start = mid + 1
    return 0
            

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

# print(arr)
m = int(sys.stdin.readline())
# print(m)
element = list(map(int, sys.stdin.readline().split()))
for i in range(m):
    print(binary_search(element[i], arr))
