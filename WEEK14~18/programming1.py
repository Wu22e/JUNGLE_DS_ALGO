def solution(table, languages, preference):

    score = [[0 for _ in range(len(languages))] for _ in range(5)]
    arr = [0] * 5
    table.sort()
    # print(table)
    for i in range(5):
        arr[i] = table[i].split(" ")
    for i in range(5):
        for j in range(len(languages)):
            for k in range(1, len(arr)+1):
                if languages[j] == arr[i][k]:
                    score[i][j] = 6-k
    # print(score)
    sum = [0 for _ in range(5)]
    for i in range(5):
        for j in range(len(preference)):
            sum[i] += score[i][j] * preference[j]
    # print(sum)
    # print(sum.index(max(sum)))
    # print(arr[sum.index(max(sum))][0])
    return arr[sum.index(max(sum))][0]
        


table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["JAVA", "JAVASCRIPT"]
preference = [7, 5]

print(solution(table, languages, preference))
# solution(table, languages, preference)






#["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
# ["PYTHON", "C++", "SQL"]
# [7, 5, 5]