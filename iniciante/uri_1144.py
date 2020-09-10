n = int(input())
x = 1

while x <= n:
    x2 = x * x
    x3 = x2 * x
    
    print('%d %d %d' %(x, x2, x3))
    print('%d %d %d' %(x, x2 + 1, x3 + 1))
    
    x+= 1
