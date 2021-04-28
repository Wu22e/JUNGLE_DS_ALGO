def solution(nums):
    answer = 0
    setNums = set(nums)
    if(len(setNums) >= len(nums)//2):
        return len(nums)//2
    else:
        return len(setNums)
    return answer


nums = [3,1,2,3]
print(solution(nums))