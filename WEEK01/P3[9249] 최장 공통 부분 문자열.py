a=input()
b=input()
num = 0

maxString = ['','']
num = [0,0]

for i in range(len(b)):
    for j in range(len(b)-1):
        if len(b) <= i+j:
            break
        elif a[j] == b[j+i]:
            maxString[0] = maxString[0] + a[j]
            num[0] = num[0] + 1
        else:
            if num[1] <= num[0]:
                num[1] = num[0]
                maxString[1] = maxString[0]
                maxString[0] = ''
                num[0] = 0
            else : 
                pass

temp_num1 = num[1]
temp_maxString1 = maxString[1]
maxString = ['','']
num = [0,0]

for i in range(len(a)):
    for j in range(len(a)):
        if len(a) <= i+j or len(b)<=j:
            break
        elif  b[j] == a[j+i]:
            maxString[0]=maxString[0] + a[j]
            num[0] = num[0] + 1
        else:
            if num[1] <= num[0]:
                num[1] = num[0]
                maxString[1] = maxString[0]
                maxString[0] = ''
                num[0] = 0
            else : 
                pass

temp_num2 = num[1]
temp_maxString2 = maxString[1]

if temp_num1>temp_num2:
    print(temp_num1)
    print(temp_maxString1)
else :
    print(temp_num2)
    print(temp_maxString2)

# 이렇게 풀면 예외처리를 너무 많이 해야함;;