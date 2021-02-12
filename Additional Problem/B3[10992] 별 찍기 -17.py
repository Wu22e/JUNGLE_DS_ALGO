n = int(input())

for i in range(n,0,-1):
    if i == n:
        print(' '*(i-1) +'*')
    elif i == 1:
        print('*'*(2*n-1))
    else:
        print(' '*(i-1) +'*'+' '*(2*(n-i)-1)+'*')

        