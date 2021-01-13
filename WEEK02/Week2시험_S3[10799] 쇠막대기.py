import sys
stick = sys.stdin.readline().strip()

stack = 0
prev = ''
result = 0

for i in stick:
    if i == '(':
        stack += 1
    else:
        stack -= 1
        if prev == '(':
            result += stack
        else:
            result += 1
    prev = i

print(result)