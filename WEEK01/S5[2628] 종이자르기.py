import sys

x,y = sys.stdin.readline().split()
x = int(x)
y = int(y)

n =int(sys.stdin.readline()) 


row = []
col = []
for i in range(n):
    a, b  = sys.stdin.readline().split() # a == 0 : 가로 a == 1 : 세로
    a = int(a)
    b = int(b)
    if a == 0:
        row.append(b)
    else:
        col.append(b)

row.sort()
col.sort()


if len(row)>=1:
    if row[0] > y-row[len(row)-1]:
        maxDistY = row[0]
    else :
        maxDistY = y-row[len(row)-1]

    for i in range(len(row)):
        if i == len(row) - 1:
            break
        if maxDistY < row[i+1] - row[i]:
            maxDistY = row[i+1] - row[i]
else:
    maxDistY = y


if len(col)>=1:
    if col[0] > x-col[len(col)-1]:
        maxDistX = col[0]
    else:
        maxDistX = x-col[len(col)-1]

    for i in range(len(col)):
        if i == len(col) - 1:
            break
        if maxDistX < col[i+1] - col[i]:
            maxDistX = col[i+1] - col[i]
else:
    maxDistX = x

# print(maxDistX)
# print(maxDistY)
print ( maxDistX * maxDistY )
        


    