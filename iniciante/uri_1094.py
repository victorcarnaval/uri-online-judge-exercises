quantity = int(input())

rabbit = 0
frog = 0
mouse = 0
total = 0

while quantity > 0:
    [number, animal] = input().split()

    if animal == 'C':
        rabbit += int(number)
    elif animal == 'S':
        frog += int(number)
    elif animal == 'R':
        mouse += int(number)

    total += int(number)
    quantity -= 1

print('Total: %d cobaias' %total)
print('Total de coelhos: %d' %rabbit)
print('Total de ratos: %d' %mouse)
print('Total de sapos: %d' %frog)
print('Percentual de coelhos: %.2f %%' %(rabbit * 100 / total))
print('Percentual de ratos: %.2f %%' %(mouse * 100 / total))
print('Percentual de sapos: %.2f %%' %(frog * 100 / total))
