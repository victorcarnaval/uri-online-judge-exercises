n = int(input())
fibonacci = []

while n > 0:
    i = len(fibonacci)
    
    if i == 0:
        fibonacci.append(0)
    elif i == 1:
        fibonacci.append(1)
    else:
        current_number = fibonacci[i - 1] + fibonacci[i - 2]
        fibonacci.append(current_number)
    
    n -= 1

print(*fibonacci)
