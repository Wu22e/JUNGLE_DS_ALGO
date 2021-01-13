import sys

def bubbleSort(a):
    for i in range(len(a)-1):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1] :
                temp = a[j]
                a[j]=a[j+1]
                a[j+1]=temp



n = int(sys.stdin.readline())

a = []
for i in range(n):
    a.append(int(sys.stdin.readline()))

bubbleSort(a)
for i in range(len(a)):
    print(a[i])
