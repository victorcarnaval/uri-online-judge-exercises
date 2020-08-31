quantity = int(input())
numbers_in = 0
numbers_out = 0

while (quantity > 0):
    number = int(input())
    if number >= 10 and number <= 20:
        numbers_in += 1
    else:
        numbers_out += 1
    quantity -= 1

print('%d in' %numbers_in)
print('%d out' %numbers_out)
