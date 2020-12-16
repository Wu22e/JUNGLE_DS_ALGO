import sys

a=[]

sum =0

for i in range(9):
    a.append(int(sys.stdin.readline()))
    sum = sum + a[i]




for i in range(9):
    for j in range(1+i,9,1):
        if i == 8:
            break
        if sum-a[i]-a[j] == 100:
            if i<j:
                index1=i
                index2=j
            else:
                index1=j
                index2=i

del a[index1]
del a[index2-1]

a.sort()


for i in range(len(a)):
    print(a[i])

# # 디버깅 코드

# for i in range(8,9,1):
#     print(i)