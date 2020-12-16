# # n,x=input().split()
# n=input()
# n=int(n)
# # x=int(x)

# for i in range(n):
#     a=input().split()
#     a=int(a)
#     print(a)
#     # if a<x:
#     #     print(a)


############### 위에 다시 해보기 (map 안쓰고!)

n,x=map(int,input().split())
a=list(map(int,input().split()))

for i in range(n):
    if a[i]<x:
        print(a[i], end=' ')