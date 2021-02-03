import sys
input = sys.stdin.readline

last_day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

x, y = map(int, input().split())

change_day = x*last_day[x]