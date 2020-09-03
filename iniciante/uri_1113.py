while True:
    [n1, n2] = [int(x) for x in input().split()]

    if n1 == n2:
        break

    if n1 < n2:
        print('Crescente')
    else:
        print('Decrescente')
