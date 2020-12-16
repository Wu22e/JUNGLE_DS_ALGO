import math 

a,b,v=input().split()
a = int(a)
b = int(b)
v = int(v)

day = math.ceil((v-a)/(a-b)) + 1

print(day)

