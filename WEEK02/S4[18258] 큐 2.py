# # 1번째 방법 : 시간 초과
# import sys
# queue =[]

# n = int(sys.stdin.readline())
# for i in range(n):
#     command = sys.stdin.readline().split()
#     if command[0] == 'push':
#         queue.append(command[1])

#     elif command[0] == 'pop':
#         if len(queue) == 0:
#             print(-1)
#         else:
#             print(queue[0])
#             queue.pop(0)

#     elif command[0] == 'size':
#         print(len(queue))

#     elif command[0] == 'empty':
#         if len(queue) == 0:
#             print(1)
#         else:
#             print(0)

#     elif command[0] == 'front':
#         if len(queue) == 0:
#             print(-1)
#         else:
#             print(queue[0])

#     else:
#         if len(queue) == 0:
#             print(-1)
#         else:
#             print(queue[-1])

# 2번째 방법
import sys

queue = [0] * 2000001
head = 0
tail = 0
def push(num):
    global tail
    queue[tail] = num
    tail += 1

def pop():
    global head
    head +=1

def front():
    return queue[head]

def back():
    return queue[tail-1]

n = int(sys.stdin.readline())
for i in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        push(command[1])
    elif command[0] == 'pop':
        if tail - head == 0:
            print(-1)
        else:
            print(front())
            pop()
    elif command[0] == 'size':
        print(tail - head)
    elif command[0] == 'empty':
        if tail - head == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if tail - head == 0:
            print(-1)
        else:
            print(front())
    else:
        if tail - head == 0:
            print(-1)
        else:
            print(back())
    

