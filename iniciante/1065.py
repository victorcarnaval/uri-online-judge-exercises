pair_numbers = []
x = 5

while x > 0:
    number = float(input())
    if number % 2 == 0:
        pair_numbers.append(number)
    x -=1
    
print('%d valores pares' %len(pair_numbers))
