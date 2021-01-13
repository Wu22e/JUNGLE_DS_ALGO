import sys


card =[0] * 1000001
head = 0
tail = 0

def push(num):
    global tail
    card[tail] = num
    tail += 1

def pop():
    global head
    head +=1

def front():
    return card[head]

def back():
    return card[tail-1]

n = int(sys.stdin.readline())
for i in range(1,n+1):
    push(i)


while True:
    if tail - head == 1:
        print(front())
        break
    pop()
    if tail - head == 1:
        print(front())
        break
    else:
        save = front()
        pop()
        push(save)


