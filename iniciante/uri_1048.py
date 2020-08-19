salario = float(input())

if salario <= 400:
    percent = 15
elif salario > 400 and salario <= 800:
    percent = 12
elif salario > 800 and salario <= 1200:
    percent = 10
elif salario > 1200 and salario <= 2000:
    percent = 7
else:
    percent = 4

reajuste = salario * (percent / 100)

print('Novo salario: %.2f' %(salario + reajuste))
print('Reajuste ganho: %.2f' %reajuste)
print('Em percentual: %d %%' %percent)
