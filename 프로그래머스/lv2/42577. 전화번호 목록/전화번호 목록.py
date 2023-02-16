# def solution(phone_book): ### 효율성 문제로 과락
#     count = 0
#     phone_book = sorted(phone_book,key = lambda x:len(x))
#     for i in range(len(phone_book)-1):
#         if i+1 < len(phone_book):
#             for j in range(i+1,len(phone_book)):
#                 if phone_book[i] == phone_book[j][:len(phone_book[i])]:
#                     return False
#     return True

def solution(phone_book): 
    count = 0
    phone_book = sorted(phone_book)
    for i in range(len(phone_book)-1):
            if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
                return False
    return True