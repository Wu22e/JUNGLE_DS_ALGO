# 리스트에 어펜드 한 방식

# import sys

# n = int(sys.stdin.readline())

# image = [list(map(int,input())) for _ in range(n)]
# result = []

# def isQuad(x, y, n): # x: 행 , y; 열, n : 영상 크기
#     temp = image[x][y]
#     flag = False
#     for i in range(x, x+n):
#         if flag:
#             break
#         for j in range(y, y+n):
#             if image[i][j] != temp:
#                 result.append('(')
#                 isQuad(x, y, n//2) # 왼쪽 위
#                 isQuad(x, y+n//2, n//2) # 오른쪽 위
#                 isQuad(x+n//2, y, n//2) # 왼쪽 아래
#                 isQuad(x+n//2, y+n//2, n//2) # 오른쪽 아래
#                 result.append(')')
#                 flag = True
#                 break
    
#     if flag == False:
#         if image[x][y] == 1:
#             result.append(1)
#         else:
#             result.append(0)



# isQuad(0,0,n)

# resultString = [str(x) for x in result]


# print(''.join(resultString))

# 리스트에 어펜드 하지않고 스트링으로 바로 받아서 출력하는 방식
import sys

n = int(sys.stdin.readline())

image = [list(map(int,input())) for _ in range(n)]
result = []

def isQuad(x, y, n): # x: 행 , y; 열, n : 영상 크기
    temp = image[x][y]
    string = ''
    flag = False
    for i in range(x, x+n):
        if flag:
            break
        for j in range(y, y+n):
            if image[i][j] != temp:
                n = n//2
                # result.append('(')
                string += '('
                string += isQuad(x, y, n) # 왼쪽 위
                string += isQuad(x, y + n, n) # 오른쪽 위
                string += isQuad(x + n, y, n) # 왼쪽 아래
                string += isQuad(x + n, y + n, n) # 오른쪽 아래
                # result.append(')')
                string += ')'
                flag = True
                break
    
    if flag == False:
        if image[x][y] == 1:
            string += '1'
        else:
            string += '0'
    return string

print(isQuad(0,0,n))
