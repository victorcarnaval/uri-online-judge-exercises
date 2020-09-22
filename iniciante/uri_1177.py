t = int(input())
n = []
x = 0

for k in range(1000):
    if x == t:
        x = 0

    n.append(x)
    x += 1

for idx, val in enumerate(n):
    print('N[%d] = %d' %(idx, val))
