n = int(input())

while n > 0:
    number = int(input())
    x = 1
    dividers = 0
    
    while x <= number:
        if number % x == 0:
            dividers += 1
        x += 1

    if dividers == 2:
        print('%d eh primo' %number)
    else:
        print('%d nao eh primo' %number)
    
    n -= 1
