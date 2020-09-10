while True:
    x = int(input())

    if x == 0:
        break;
    
    numbers = []
    [numbers.append(j) for j in range(1, x + 1)]
    print(' '.join([str(k) for k in numbers]))
        
