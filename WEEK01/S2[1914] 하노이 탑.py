

def hanoi(num,reference,destination,cnt=0):
    if num == 0:
        return
    
    stopover = 6 - reference - destination
    
    hanoi(num-1,reference,stopover)

    print(reference,destination)

    hanoi(num-1, stopover,destination)

n = int(input())
print(2**n-1)
hanoi(n, 1,3)
# print(cnt)