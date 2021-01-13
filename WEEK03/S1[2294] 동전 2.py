import sys
n, k = map(int,sys.stdin.readline().split())
val = [] # 화폐의 가치(단위)

# N개의 화폐 단위 정보를 입력 받기
for _ in range(n):
    val.append(int(input()))

# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
dp = [10001] * (k + 1)

# 다이나믹 프로그래밍 진행 (바텀 업)
dp[0] = 0
for i in range(n):
    for j in range(val[i], k+1):
        if dp[j - val[i]] != 10001: # (i-k)원을 만드는 방법이 존재하는 경우
            dp[j] = min(dp[j], dp[j - val[i]] + 1)

# 계산된 결과 출력
if dp[k] == 10001: # 최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(dp[k])



