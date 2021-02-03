import heapq
import sys

input = sys.stdin.readline

n = int(input().rstrip())

heap=[]

for _ in range(n):
    row_window = list(map(int, input().rstrip().split(" ")))
    for i in row_window:
        heapq.heappush(heap, i)

    while(len(heap) > n):
        heapq.heappop(heap)

print(heapq.heappop(heap))
