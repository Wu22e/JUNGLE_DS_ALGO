def solution(inp_str):
    # answer = []
    # return answer
    special_char = ['~','!','@','#','$','%','^','&','*']

    bool flag1 = False
    bool flag2 = False
    bool flag2_1 = False
    bool flag2_2 = False
    bool flag2_3 = False
    bool flag2_4 = False


    bool flag3 = False
    bool flag4 = False
    
    if len(inp_str) >= 8 && len(inp_str) <= 15:
        flag1 = True
    else:
        flag1 = False
    
    for i in range(len(inp_str)):
        if ord(i) >= ord('A') && ord(i) <= ord('Z'):
            flag2_1 = True
        else:
            flag2 = False
    for i in range(len(inp_str)):
        if ord(i) >= ord('a') && ord(i) <= ord('z'):
            flag2_2 = True
        else:
            flag2 = False
    for i in range(len(inp_str)):
        if ord(i) >= ord('0') && ord(i) <= ord('9'):
            flag2_3 = True
        else:
            flag2 = False
    for i in range(len(inp_str)):
        if i in special_char:
            flag2_4 = True
        else:
            flag2 = False
    


#3종류 이상 포함
# 같은문자 4개이상 연속 x
# 같은문자 5개이상 포함 x


# inp_str	result
# "AaTa+!12-3"	[2]
# "aaaaZZZZ)"	[2, 3, 4]
# "CaCbCgCdC888834A"	[1, 4, 5]
# "UUUUU"	[1, 3, 4, 5]
# "ZzZz9Z824"	[0]