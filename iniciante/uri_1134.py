alcohol = 0
gasoline = 0
diesel = 0

while True:
    product = int(input())

    if product == 1:
        alcohol += 1
    elif product == 2:
        gasoline += 1
    elif product == 3:
        diesel += 1
    elif product == 4:
        break

print('MUITO OBRIGADO')
print('Alcool: %d' %alcohol)
print('Gasolina: %d' %gasoline)
print('Diesel: %d' %diesel)
