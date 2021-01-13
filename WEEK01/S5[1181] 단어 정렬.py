#### 1번방법(실패) 뭐가 문젠지 감은 옴 근데 어케 고쳐야할지 모르겟음

# import sys , string



# def bubbleSort(a):

#     for i in range(len(a)-1):
#         if len


#     for i in range(len(a)-1):
#         for j in range(len(a)-i-1):
#             if a[j] == a[j+1]:
#                     del a[j]
#                     continue
#             if len(a[j]) > len(a[j+1]) :
#                 a[j],a[j+1] = a[j+1],a[j]
#             elif len(a[j])==len(a[j+1]) :
#                 for k in range(len(a[j])):
#                     if ord(a[j][k]) == ord(a[j+1][k]):
#                         continue
#                     elif ord(a[j][k])>ord(a[j+1][k]):
#                         a[j],a[j+1]=a[j+1],a[j]
#                         break


# n = int(sys.stdin.readline())
# a = []
# for i in range(n):
#     a.append(input())

# print(a)

# bubbleSort(a)

# print(a)

# # 디버깅 코드
# # print(ord("zx")) # 오류뜸
# # print(ord('n'))
# # print(ord('i'))

## 2번 방법 파이썬 코드 적극 이용



# import sys , string

# n = int(sys.stdin.readline())
# a = []
# for i in range(n):
#     a.append(input())

# new_a = list(set(a))
# print(new_a)

# b=[]

# b.append