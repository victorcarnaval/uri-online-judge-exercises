[x, y] = [int(x) for x in input().split()]

numbers = []
for k in range(1, y + 1):       
    numbers.append(k)

    if len(numbers) == x:
        print('%s' %(' '.join([str(j) for j in numbers])))
        numbers = []
