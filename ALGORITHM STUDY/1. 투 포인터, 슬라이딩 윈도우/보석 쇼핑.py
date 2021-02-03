# # 어떻게 start end포인트를 움직여야 할 지 모르겠음.
# def solution(gems):
#     answer = []
#     my_set = set(gems)
#     list_gems = list(my_set)
#
#     start = 0
#     end = 1
#
#     newList = []
#     flag = False
#     while True:
#         # if flag:
#         #     break
#         newList = gems[start: end]
#
#         if len(newList) >= len(list_gems):
#             for i in range(len(list_gems)):
#                 if list_gems[i] not in newList:
#                     end += 1
#                     break
#
#                 answer.append([start, end])
#                 flag = True
#                 break
#         else:
#             end += 1
#
#     print(newList)
#
#
#
#     return answer
#
# gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
#
# k = solution(gems)
# print(k)

def solution(gems):
    answer = []
    my_set = set(gems)
    list_gems = list(my_set)

    start = 0
    end = 1

    newList = []
    flag = False
    while True:
        # if flag:
        #     break
        newList = gems[start: end]

        if len(newList) >= len(list_gems):
            for i in range(len(list_gems)):
                if list_gems[i] not in newList:
                    end += 1
                    break

                answer.append([start, end])
                flag = True
                break
        else:
            end += 1

    print(newList)



    return answer

gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]

k = solution(gems)
print(k)

