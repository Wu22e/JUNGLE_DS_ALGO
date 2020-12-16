x,y,w,h = input().split()
x=int(x)
y=int(y)
w=int(w)
h=int(h)

dist1=w-x
dist2=h-y

if w-x <= x:
    dist1=w-x
else :
    dist1=x

if h-y <= y:
    dist2=h-y
else :
    dist2=y

if dist1>=dist2:
    dist=dist2
elif dist1<=dist2:
    dist=dist1
else :
    pass

print(dist)