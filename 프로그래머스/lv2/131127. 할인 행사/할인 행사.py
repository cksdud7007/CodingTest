from collections import Counter, deque
import itertools

def solution(want, number, discount):
    want_dict = {}

    for i in range(len(want)):
        want_dict[want[i]] = number[i]

    discount = deque(discount)
    cnt = 0
    while discount:
        
        check = list(itertools.islice(discount, 0, 10))
        check_dict = Counter(check)
        sub_cnt = 0
        for i in set(check):
            if i in want and want_dict[i] == check_dict[i]:
                sub_cnt += 1
            else:
                break
                
        if sub_cnt == len(want):
            cnt += 1
        discount.popleft()
    return cnt