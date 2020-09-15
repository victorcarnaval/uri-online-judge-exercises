n = int(input())

while n > 0:
    [x, y] = [int(x) for x in input().split()]
    total = 0
    
    if x % 2 == 0:
        x += 1
        
    while y > 0:
        total += x
        x += 2
        y -= 1

    print(total)
    
    n -= 1
