n = int(input())
weights = [2, 3, 5]

while n > 0:
    numbers = [float(x) for x in input().split()]
    total = 0
    i = 0
    
    for x in numbers:
        total += x * weights[i]
        i += 1
        
    print('%.1f' %(total / sum(weights)))
        
    n -= 1
