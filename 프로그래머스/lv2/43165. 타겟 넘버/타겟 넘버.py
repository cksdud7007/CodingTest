def solution(numbers, target):
    count = 0 
    def operate(numbers,target,idx=0):
        if len(numbers) > idx:
            numbers[idx] *= 1
            operate(numbers,target,idx+1)
            
            numbers[idx] *= -1
            operate(numbers,target,idx+1)
        
        else:
            if sum(numbers) == target:
                nonlocal count
                count += 1
        
    operate(numbers,target)
    return count