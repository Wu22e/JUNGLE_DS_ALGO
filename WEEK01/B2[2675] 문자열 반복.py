###########################################
#                                         #
#                                         #
# 문제에서 QR CODE 예시로 설명해준 이유?? #
#                                         #
#                                         #
###########################################


testcase = int(input())
new_s=''
for i in range(testcase):
    s=list(input().split())
    for j in range(len(s[1])):
        for k in range(int(s[0])):
            new_s=new_s+str(s[1][j])
    print(new_s)
    new_s=''



# 디버깅 코드

# s=list(input().split())
# print(s)

# st=''
# print(st+'1')