def solution(people, limit):
    people = sorted(people,reverse=True)
    count = 0
    i = 0
    j = len(people) - 1
    while i <= j:
        count += 1
        if people[j] + people[i] <= limit:
            j -= 1
        i += 1
        
    return count