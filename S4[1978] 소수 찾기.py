n = int(input())
num=list(map(int,input().split()))
prime_check = 0

cnt=0

for i in range(n):
    if num[i] == 2:
            cnt = cnt + 1
    elif num[i] > 2:
        for j in range(num[i]):
            if num[i] % (j+1) == 0:
                prime_check = prime_check + 1
            else:
                pass
        if prime_check == 2:
                cnt = cnt + 1
                prime_check = 0
        else:
            prime_check = 0
    else:
        pass
print(cnt)
        

    