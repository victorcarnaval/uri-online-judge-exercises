total_cases = int(input())

while total_cases > 0:
    n = int(input())
    x = 0
    fibonacci = []

    while x <= n:
        if x > 1:
            total = fibonacci[x - 1] + fibonacci[x - 2]
            fibonacci.append(total)
        else:
            fibonacci.append(x)
        x += 1

    print('Fib(%d) = %d' %(n, fibonacci[-1]))
    total_cases -= 1
