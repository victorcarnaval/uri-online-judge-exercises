n = int(input())
cont = 1
total = n

while cont < n:
    total *= n - cont
    cont += 1

print(total)
