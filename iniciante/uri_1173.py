n = int(input())
v = [n]
x = 1

while x <= 9:
    n = v[x - 1] * 2
    v.append(n)
    x += 1

for idx, val in enumerate(v):
    print('N[%d] = %d' % (idx, val))
