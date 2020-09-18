n = int(input())

while n  > 0:
    number = int(input())
    x = 1
    total = 0

    while x < number:
        if number % x == 0:
            total += x
        x += 1

    if number == total:
        print('%d eh perfeito' % number)
    else:
        print('%d nao eh perfeito' % number)

    n -= 1
