n = int(input())

for i in range(n):
    print(' '*i + '*'*(2*n-2*i-1))

for i in range(n-2,-1,-1):
    print(' '*i + '*'*(2*n-2*i-1))

# 이 문제는 공백없이 출력해야 안틀림