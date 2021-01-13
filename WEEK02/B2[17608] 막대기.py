import sys

stackStick = []
n = int(sys.stdin.readline())
for i in range(n):
    stackStick.append(int(sys.stdin.readline()))

# maxStick = max(stackStick)
maxStick = stackStick[-1]

cnt = 1
for i in range(len(stackStick) - 1, -1, -1):
    if stackStick[i] > maxStick:
        cnt += 1
        maxStick = stackStick[i]
        stackStick.pop()
    else:
        stackStick.pop()

print(cnt)


    
     
