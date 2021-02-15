import sys

input = sys.stdin.readline

testcase = int(input())

for i in range(testcase):
    n = int(input())
    for j in range(2):
        score = list(map(int,input().split()))
        print(score)
