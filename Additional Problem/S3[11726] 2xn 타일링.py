# 최적화 하기 전 dp
# n = int(input())

# dp = [0 for _ in range(n+1)]

# dp[1] = 1

# if n >= 2: # 예외 처리
#     dp[2] = 2

# for i in range(3, n+1):
#     dp[i] = dp[i-1] + dp[i-2]

# print(dp[n]%10007)

# 메모리 최적화가 맞긴함? 1000개랑 3개랑 뭐가다른지 잘모르겟음
n = int(input())

prev = 1
curr = 2

for i in range(3, n+1):
    next = prev + curr
    prev = curr
    curr = next

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    print(next%10007)