from collections import deque
def solution(prices):
    answer = []

    queuePrices = deque(prices)

    while queuePrices:
        price = queuePrices.popleft()
        time = 0
        for i in queuePrices:
            time += 1
            if price > i:
                break
        answer.append(time)

    return answer

prices = [1,2,3,2,3]
print(solution(prices))

"asdfa" + str()