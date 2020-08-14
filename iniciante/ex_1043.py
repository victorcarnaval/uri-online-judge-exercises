[a, b, c] = [float(x) for x in input().split()]
is_triangle = True

if a + b <= c or b + c <= a or a + c <= b:
    is_triangle = False

if is_triangle:
    perimetro = a + b + c
    print('Perimetro = %.1f' % perimetro)
else:
    area = (c * (a + b)) / 2
    print('Area = %.1f' % area)
