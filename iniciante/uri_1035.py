[A, B, C, D] = [int(x) for x in input().split()]
is_accepted = False

if (B > C and D > A):
    somaCD = C + D
    somaAB = A + B
    if (somaCD > somaAB and C >= 0 and D >= 0 and A % 2 == 0):
        is_accepted = True

print('Valores aceitos' if is_accepted else 'Valores nao aceitos')
