n = int(input())

while n > 0:
    [pa, pb, ga, gb] = [x for x in input().split()]
    pa, pb = int(pa), int(pb)
    ga, gb = float(ga), float(gb)
    years = 1
    
    while years <= 100:
        pa += int(pa * ga / 100)
        pb += int(pb * gb / 100)

        if pa > pb:
            break
        years += 1
        
    if years > 100:
        print('Mais de 1 seculo.')
    else:
        print('%d anos' %years)
        
    n -= 1
