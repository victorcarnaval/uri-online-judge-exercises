maior = 0
position = 0

for x in range(100):
    n = int(input())

    if n > maior:
        maior = n
        position = x + 1
        
print(maior)
print(position)
