number = list(map(int,input().split()))

ok = True

for i in number:
    if number.count(i) == 3:
        answer = 10000 + i * 1000
        ok = False
        
    elif number.count(i) == 2:
        answer = 1000 + i * 100
        ok = False

if ok:
    answer = max(number) * 100
    
print(answer)