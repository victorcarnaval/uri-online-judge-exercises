v = []

for x in range(20):
    n = int(input())
    v.append(n)

x = 0
while x < (len(v) / 2):
    idx_aux = len(v) - x - 1
    v[x], v[idx_aux] = v[idx_aux], v[x]
    x += 1

for idx, val in enumerate(v):
    print('N[%d] = %d' %(idx, val))
