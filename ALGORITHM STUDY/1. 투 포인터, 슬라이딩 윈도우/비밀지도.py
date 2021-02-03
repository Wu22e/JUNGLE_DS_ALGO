print("10진수")
n = int(input())
x = int(input())
y = ""
print("2진수")
while x > 0:
    y = str(x % 2) + y
    x //= 2
if len(y) != n:
    for _ in range(n - len(y)):
        y = '0' + y

print(y)

# 뻘짓한 코드;
# def solution(n, arr1, arr2):
#     answer = []
    # bin1 = ""
    # bin2 = ""
    # bin1List = []
    # bin2List = []
    # for num in arr1:
    #     while num > 0:
    #         bin1 = str(num%2) + bin1
    #         num //= 2
    #     if len(bin1) != n:
    #         for _ in range(n-len(bin1)):
    #             bin1 = '0' + bin1
    #     bin1List.append(bin1)
    #     bin1 =""

    #     for num in arr2:
    #         while num > 0:
    #             bin2 = str(num%2) + bin2
    #             num //= 2
    #         if len(bin2) != n:
    #             for _ in range(n-len(bin2)):
    #                 bin2 = '0' + bin2
    #         bin2List.append(bin2)
    #         bin2 =""

    #     print(bin1List)
    #     print(bin2List)

    # return answer



    # 애도 어케 바꿔야할지모르겟음;;
#
# def solution(n, arr1, arr2):
#     answer = []
#     newarr = []
#     for i in range(n):
#         newarr.append(arr1[i] | arr2[i])
#     bin = ""
#     binList = []
#     for num in newarr:
#         while num > 0:
#             bin = str(num % 2) + bin
#             num //= 2
#         if len(bin) != n:
#             for _ in range(n - len(bin)):
#                 bin = "0" + bin
#         binList.append(bin)
#         bin = ""
#     for i in range(n):
#         binList[i] = list(binList[i])
#
#     for i in range(n):
#         for j in range(n):
#             if binList[i][j] == "1":
#                 binList[i][j] = "#"
#             else:
#                 binList[i][j] = " "
#     print(binList)
#     for i in range(n):
#         binList[i] = ",".join(binList[i])
#         binList[i] = binList[i].split(',')
#
#         # binList[i] = ",".join(binList[i])
#     print(binList)
#
#     return answer