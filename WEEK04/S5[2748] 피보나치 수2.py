# dynamic programming을 할때, 모든 계산값을 저장할 필요가 없다면
# 공간 사용을 최적화 하면 좋다!

# n = int(input())


# def fibo(n):
#     pre = 1
#     cur = 1
#     if n == 1 or n == 2:
#         return 1
#     for _ in range(n-2):
#         next = cur + pre
#         pre = cur
#         cur = next
#     return next
# print(fibo(n)%1000000)

# dp로 푸는방법은 없을까?
n = int(input())

def fibo(n):
    fib_table = [0, 1, 1]
    
    if n < 3:
        return fib_table[n]
    

    
    for i in range(3, n+1):
        fib_table.append(fib_table[i-1] + fib_table[i-2])
    
    return fib_table[n]

print(fibo(n%1000000))