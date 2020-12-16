c=int(input())
_sum=0
num=0
for i in range(c):
    n=list(map(int,input().split()))
    for j in range(n[0]):
        _sum = _sum + n[j+1]
    avg=_sum/n[0]
    
    for k in range(n[0]):
        if n[k+1]>avg:
            num=num+1
    print(format(num/n[0]*100,".3f")+'%')
    num=0
    _sum=0


# 디버깅 코드
# _sum=0
# n=[5, 50, 50, 70, 80, 100]
# print(n[0])
# for j in range(n[0]):
#     _sum = _sum + n[j+1]
# print(_sum)
# print(_sum/n[0],"%")
# _sum=0