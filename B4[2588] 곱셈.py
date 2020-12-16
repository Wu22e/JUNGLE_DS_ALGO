
a=input()
b=input()

a=int(a)
b=int(b)

location100=b//100
location10=(b-location100*100)//10
location1=b-location100*100-location10*10

print(a*location1)
print(a*location10)
print(a*location100)
print(a*b)