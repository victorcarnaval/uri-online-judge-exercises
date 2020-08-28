pair_numbers = []
x = 6

while x > 0:
    number = float(input())
    if number >= 0:
        pair_numbers.append(number)
    x -=1
    
print('%d valores positivos' %len(pair_numbers))
print('%.1f' % (sum(pair_numbers) / len(pair_numbers)))
