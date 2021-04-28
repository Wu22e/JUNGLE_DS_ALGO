def solution(phone_book):
    answer = True
    phone_book.sort() # String 이므로 사전순으로 정렬됨
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]: # 사전순으로 정렬되므로 인접한 배열끼리만 비교하면 됨
            return False
    
    return True

phone_book = ["119", "97674223", "1195524421"]
print(solution(phone_book))