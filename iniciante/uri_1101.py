while True:
    [n1, n2] = [int(x) for x in input().split()]

    if n1 <= 0 or n2 <= 0:
        break

    if n1 > n2:
        n1, n2 = n2, n1

    numbers = []
    for x in range(n1, n2 + 1):
        numbers.append(x)

    str_numbers = ' '.join(str(x) for x in numbers)
    print('%s Sum=%d' %(str_numbers, sum(numbers)))
