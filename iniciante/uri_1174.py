v = []

for x in range(100):
    n = float(input())
    v.append(n)

for idx, val in enumerate(v):
    if val <= 10:
        print('A[%d] = %.1f' %(idx, val))
