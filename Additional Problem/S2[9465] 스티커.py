import sys

input = sys.stdin.readline

testcase = int(input())

for i in range(testcase):
    n = int(input())
    score = [[int(x) for x in input().split()] for _ in range(2)]
    score[0][1] += score[1][0]
    score[1][1] += score[0][0]
    for j in range(2, n):
        score[0][j] += max(score[1][j-1], score[1][j-2])
        score[1][j] += max(score[0][j-1], score[0][j-2]) 
    print(max(score[0][n-1], score[1][n-1]))

