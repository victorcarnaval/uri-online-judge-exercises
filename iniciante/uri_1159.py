while True:
    x = int(input())
    total = 0

    if x == 0:
        break

    if x % 2 == 1:
        x += 1

    for k in range(1, 6):
        total += x
        x += 2

    print(total)
