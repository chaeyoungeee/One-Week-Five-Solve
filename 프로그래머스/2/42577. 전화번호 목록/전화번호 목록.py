def solution(phone_book):
    phone_book.sort()
    pl = len(phone_book[0])
    
    for i in range(1, len(phone_book)):
        if phone_book[i][:pl] == phone_book[i-1]:
            return False
        pl = len(phone_book[i])
    return True