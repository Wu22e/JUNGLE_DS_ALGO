import sys

def factorial(num):
    if num<=0:
        return 1
    else:
        return num*factorial(num-1)

n = int(sys.stdin.readline())

print(factorial(n))


