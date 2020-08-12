[codigo, quantidade] = [int(x) for x in input().split()]

if codigo == 1:
    total = quantidade * 4.00
    
if codigo == 2:
    total = quantidade * 4.50
    
if codigo == 3:
    total = quantidade * 5.00
    
if codigo == 4:
    total = quantidade * 2.00

if codigo == 5:
    total = quantidade * 1.50

print('Total: R$ %.2f' % total)


