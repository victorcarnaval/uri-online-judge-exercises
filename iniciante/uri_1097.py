i = 1
j = 7

while i <= 9:
    for x in range(3):
        print('I=%d J=%d' %(i, j))
        j -= 1

    j += 5
    i += 2
