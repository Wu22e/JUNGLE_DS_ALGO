import math

n = int(input())

def is_prime_number(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


for i in range(2, n+1):
    if is_prime_number(i):
        



for i in range(2, n+1):
    