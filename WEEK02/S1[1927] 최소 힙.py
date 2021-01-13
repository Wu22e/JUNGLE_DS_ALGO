import sys

heap = [0]*100005
sz = 0 # heap size

def add(x):
    global sz
    global heap
    sz += 1
    heap[sz] = x
    idx = sz
    while idx != 1:
        par = idx // 2
        if heap[par] < heap[idx]:
            break
        heap[par], heap[idx] = heap[idx], heap[par]
        idx = par

def top():
    if sz == 0:
        return 0
    return heap[1]

def pop():
    global sz
    global heap
    if sz == 0:
        return
    heap[1], heap[sz] = heap[sz], heap[1]
    sz -= 1
    idx = 1
    while 2*idx <= sz:
        if heap[2*idx] < heap[2*idx + 1] or 2*idx + 1 > sz:
            minChild = 2 * idx
        else:
            minChild = 2*idx + 1
        if heap[idx] < heap[minChild]:
            break
        heap[idx],heap[minChild] = heap[minChild],heap[idx]
        idx = minChild

n = int(sys.stdin.readline())
while n:
    n -= 1
    x = int(sys.stdin.readline())
    if x == 0:
        print(top())    
        pop()
    else:
        add(x)



