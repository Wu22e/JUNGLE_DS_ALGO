def solution(brown, yellow):
    answer = []
    area = brown + yellow
    for i in range(area, 0, -1):
        if area % i == 0:
            x = i
            y = area // x
            # print(x, y)
            if x + y == (brown + 4) / 2:
                answer.append(x)
                answer.append(y)
                break
            
    return answer