quantity = int(input())

while quantity > 0:
    n = int(input())

    if n % 2 == 0:
        result = 'EVEN'
    else:
        result = 'ODD'
        
    if n > 0:
        result = result + ' POSITIVE'
    elif n < 0:
        result = result + ' NEGATIVE'
    else:
        result = 'NULL'

    print(result)
        
    quantity -= 1
