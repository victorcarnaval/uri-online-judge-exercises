x = int(input())
z = x
total_sum = 0
cont = 0

while z <= x:
    z = int(input())

while total_sum < z:
    total_sum += x
    x += 1
    cont += 1

print(cont)
