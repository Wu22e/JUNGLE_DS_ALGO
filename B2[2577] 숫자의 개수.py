a=int(input())
b=int(input())
c=int(input())

result = str(a*b*c)
# print(len(result))
num=0

for i in range(10):
    for j in range(len(result)):
        if result[j]==str(i):
            num=num+1
    print(num)
    num=0


# 한번 탐색한 걸 다시 탐색하지 않게하는방법 없을까??



