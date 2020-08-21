salario = float(input())

if salario <= 2000:
    print('Isento')
    
elif salario > 2000 and salario <= 3000:
    salario -= 2000
    print('R$ %.2f' %(salario * 0.08))
    
elif salario > 3000 and salario <= 4500:
    salario -= 3000
    print('R$ %.2f' %(salario * 0.18 + 1000 * 0.08))
    
else:
    salario -= 4500
    print('R$ %.2f' %(salario * 0.28 + 1500 * 0.18 + 1000 * 0.08))
