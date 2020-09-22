x = float(input())
n = [x]

for k in range(99):
    x /= 2
    n.append(x)    

for idx, val in enumerate(n):
    print('N[%d] = %.4f' %(idx, val))
