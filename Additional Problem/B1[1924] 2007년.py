import sys
input = sys.stdin.readline

last_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_of_week = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
x, y = map(int, input().split())

change_day = 0

for i in range(x-1):
    change_day += last_day[i]
change_day += y - 1


print(day_of_week[change_day%7])