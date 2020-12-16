## 1번 방법 (실패..)

# def stringChange(s):
#     for i in range(len(s)):
#         temp = s[i]
#         s[i] = s[len(s)-1-i]
#         s[len(s)-1-i]=temp
#         if i>=len(s)//2:
#             break
#     return s

# a,b = input().split()

# new_a=int(stringChange(a))
# new_b=int(stringChange(b))

# if new_a>new_b:
#     print(new_a)
# else:
#     print(new_b)

# 디버깅 코드
# s="123"
# print(s)
# for i in range(len(s)):
#     temp = s[i]
#     s[i] = s[len(s)-1-i]
#     s[len(s)-1-i]=temp
#     if i>=len(s)//2:
#         break
# print(s)

#### 2번 방법 (인터넷 참고했음)

def stringChange(s):
    s_reverse=''
    for char in s:
        s_reverse = char + s_reverse
    return s_reverse


a,b = input().split()

new_a=int(stringChange(a))
new_b=int(stringChange(b))

if new_a>new_b:
    print(new_a)
else:
    print(new_b)

#### 3번 방법 (미완)

# def stringChange(s):
#     s_reverse=list(s)
#     s_reverse.reverse()
#     return s_reverse


# a,b = input().split()

# new_a=int(stringChange(a))
# new_b=int(stringChange(b))

# if new_a>new_b:
#     print(new_a)
# else:
#     print(new_b)

#### 4번 방법 (블로그 참고)

## 참고 사이트 : https://itholic.github.io/python-reverse-string/