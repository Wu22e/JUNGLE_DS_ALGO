import sys, copy

input = sys.stdin.readline

n = int(input())

min_a, min_b, min_c = list(map(int, input().split()))
max_a, max_b, max_c = min_a, min_b, min_c
maxVal = 0
minVal = 0
if n == 1:
    print(max(min_a,min_b,min_c), min(min_a,min_b,min_c))
else:
    for i in range(n-1):
        score_max = list(map(int, input().split()))
        score_min = copy.deepcopy(score_max)

        score_max[0] += max(max_a, max_b)
        score_max[1] += max(max_a, max_b, max_c)
        score_max[2] += max(max_b, max_c)

        score_min[0] += min(min_a, min_b)
        score_min[1] += min(min_a, min_b, min_c)
        score_min[2] += min(min_b, min_c)

        max_a = score_max[0]
        max_b = score_max[1]
        max_c = score_max[2]
        maxVal = max(score_max)

        min_a = score_min[0]
        min_b = score_min[1]
        min_c = score_min[2]
        minVal = min(score_min)
    print(maxVal, minVal)

