# 1번 방법 (시간초과 남 ..)
# def isPrime(num):
#     prime_check = 0
#     if num == 2:
#         return True
#     elif num >2:
#         for i in range(num):
#             if num % (i+1) == 0:
#                 prime_check = prime_check + 1
#             else:
#                 pass
#         if prime_check == 2:
#             return True
#         else:
#             return False
#     else:
#         return False



# testcase = int(input())

# cnt = 0

# for i in range(testcase):
#     n = int(input())
#     comp = {}
#     if n == 4:
#         print("2 2")
#     else:
#         for j in range(n,2,-1):
#             if isPrime(j):
#                 if isPrime(n-j):
#                     if j<=n-j :
#                         comp[(n-j)-j] = [j, n-j]
#                     else: 
#                         continue
#                 else:
#                     continue
#             else:
#                 continue
#         a=sorted(comp.items(),key=lambda x:x[0])
#         print(list(comp.values())[0][0],list(comp.values())[0][1])


##### 2번 방법
            
import sys

def isPrime(num):
    prime_check = 0
    if num == 2:
        return True
    elif num > 2:
        for i in range(num):
            if num % (i+1) == 0:
                prime_check = prime_check + 1
            else:
                pass
            if prime_check >= 3:
                return False
        if prime_check == 2:
            return True
        else:
            return False
    else:
        return False



testcase = int(sys.stdin.readline())

cnt = 0

for i in range(testcase):
    n = int(sys.stdin.readline())
    comp = {}
    if n == 4:
        print("2 2")
    else:
        for j in range(int(n/2),2,-1):
            if isPrime(j) and isPrime(n-j):
                if j<=n-j :
                    print(j,n-j)
                    break
                else:
                    pass
            else:
                pass

            







