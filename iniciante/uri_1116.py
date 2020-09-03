quantity = int(input())

while quantity > 0:

    [n1, n2] = [int(x) for x in input().split()]

    if n2 == 0:
        print('divisao impossivel')
    else:
        print(n1 / n2)
    
    quantity -= 1
