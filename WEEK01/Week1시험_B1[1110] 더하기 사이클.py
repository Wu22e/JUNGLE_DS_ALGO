n = int(input())

location1 = n%10
location10 = n//10

cnt = 0
newNum = -1

while n != newNum:
    pasteNum = (location10+location1)
    newNum = int(str(location1)+str(pasteNum%10))
    location1 = newNum%10
    location10 = newNum//10
    cnt += 1

print(cnt)


# 디버깅 코드

# print(int(str(1) + str(2)))
# # print(1)