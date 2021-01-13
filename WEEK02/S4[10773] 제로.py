import sys

k = int(sys.stdin.readline())

moneyStack = []

for i in range(k):
    money = int(sys.stdin.readline())
    if money == 0:
        moneyStack.pop()
        continue
    moneyStack.append(money)

print(sum(moneyStack))
