n, k = map(int,input().split())

count = 0

coin_type = []
for _ in range(n):
    coin_type.append(int(input()))

coin_type.sort(reverse=True)

for coin in coin_type:
    count += k // coin
    k %= coin

print(count)


