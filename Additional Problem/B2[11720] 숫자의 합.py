import sys

input = sys.stdin.readline

n = int(input())

string = list(map(int,input().rstrip()))
print(sum(string))
