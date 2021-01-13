testcase = int(input())

checkList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
remember = []
for i in range(testcase):
    n =list(input().split())
    location100 = n[0]//100
    location10  = n[0]%100//10
    location1 = n[0]%10

    if n[1] == 3 and n[2] == 0:
        print(1)
        break

    elif n[1] == 0 and n[2] == 3:
        for j in range(6):
            if j == location1 or j == location10 or j == location100:
                continue
            del checkList[j]
            
    elif n[1] == 2 and n[2] == 0:
        remember.append(location100)
        remember.append(location10)
        remember.append(location1)

    elif n[1] == 0 and n[2] == 0:
        for j in range(3):
            del checkList[location1]
            del checkList[location10]
            del checkList[location100]




