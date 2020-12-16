testcase=int(input())
num=0
_sum=0
for i in range(testcase):
    a=input()
    for j in range(len(a)):
        if a[j] == 'O':
            num=num+1
            _sum=_sum+num
        
        elif a[j] == 'X':
            num=0
    print(_sum)
    _sum=0
    num=0    

# 디버깅 코드
# num=0
# _sum=0

# a='OOOOXOOOOXOOOOX'
# for j in range(len(a)):
#     if a[j] == 'O':
#         num=num+1
#         _sum=_sum+num    
#     elif a[j] == 'X':
#         num=0
# print(_sum)
  

