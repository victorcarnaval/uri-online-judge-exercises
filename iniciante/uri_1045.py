sides = [float(x) for x in input().split()]
j = 0

while j < len(sides):
    k = j
    while k < len(sides):
        if sides[j] < sides[k]:
            sides[j], sides[k] = sides[k], sides[j]
        k += 1
    j += 1

[a, b, c] = sides

if a >= b + c:
    print('NAO FORMA TRIANGULO')
else:
    square_a = a ** 2
    sum_square_b_c = b ** 2 + c ** 2

    if square_a == sum_square_b_c:
        print('TRIANGULO RETANGULO')
    if square_a > sum_square_b_c:
        print('TRIANGULO OBTUSANGULO')
    if square_a < sum_square_b_c:
        print('TRIANGULO ACUTANGULO')
    if a == b and a == c:
        print('TRIANGULO EQUILATERO')
    if (a == b and a != c) or (b == c and b != a) or (a == c and a != b):
        print('TRIANGULO ISOSCELES')
