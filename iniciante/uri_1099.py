quantity = int(input())

while quantity > 0:
    [n1, n2] = [int(x) for x in input().split()]

    if n1 > n2:
        n1, n2 = n2, n1

    total = 0
    for x in range(n1 + 1, n2):
        if x % 2 != 0:
            total += x
    print(total)
    
    quantity -= 1
