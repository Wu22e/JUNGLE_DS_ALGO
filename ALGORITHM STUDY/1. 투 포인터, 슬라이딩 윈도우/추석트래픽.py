import sys

input = sys.stdin.readline

def solution(lines):
    answer = 0
    for i in range(len(lines)):
        newLines = lines[i].split(' ')
        # endlist = newLines[1].split(':')
        endtime = float(endlist[0])*3600 + float(endlist[1])*60 + float(endlist[2])
        # taketime = endtime - float(newLines[2][:-1])
        # print(taketime)
        print(endlist)
        # print(endtime)
        # print(newLines)
    answer = newLines[0]
    return answer

lines = input()
# print(lines)
print(solution(lines))