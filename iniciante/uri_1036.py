[a, b, c] = [float(x) for x in input().split()]
is_calculable = True

delta = b**2 - 4 * a * c

if (a <= 0 or delta < 0):
    is_calculable = False

if (is_calculable):
    x1 = (-b + delta ** (1/2)) / (2 * a)
    x2 = (-b - delta ** (1/2)) / (2 * a)

    print('R1 = %.5f' % x1)
    print('R2 = %.5f' % x2)
else:
    print('Impossivel calcular')
