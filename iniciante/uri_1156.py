s = 0
x = 1
y = 1

while x <= 39:
    s += x / y
    x += 2
    y *= 2
    
print('%.2f' % s)
