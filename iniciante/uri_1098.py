i = 0
j = 1

while i <= 2:
    for x in range(3):
        i = round(i, 10)
        if i > int(i):
            print('I=%.1f J=%.1f' %(i, j))
        else:
            print('I=%d J=%d' %(i, j))
        j += 1
        
    i += 0.2
    j = 1 + i
