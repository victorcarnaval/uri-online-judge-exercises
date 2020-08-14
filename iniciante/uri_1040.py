notas = [float(x) for x in input().split()]
pesos = [2, 3, 4, 1]
total_notas = 0
i = 0
is_exame = False

while i < len(notas):
    total_notas += notas[i] * pesos[i]
    i += 1

media = total_notas / 10

print('Media: %.1f' % media)

if media >= 7:
    print('Aluno aprovado.')
elif media >= 5 and media <= 6.9:
    print('Aluno em exame.')
    is_exame = True
else:
    print('Aluno reprovado.')

if is_exame:
    nota_exame = float(input())
    print('Nota do exame: %.1f' % nota_exame)

    media = (nota_exame + media) / 2

    if media >= 5:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')

    print('Media final: %.1f' % media)
    
