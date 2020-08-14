n = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print('NOTAS:')
for nota in notas:
    x = int(round(n, 2) / nota)
    n -= x * nota
    print("%d nota(s) de R$ %.2f" % (x, nota))

print('MOEDAS:')
for moeda in moedas:
    x = int(round(n, 2) / moeda)
    n -= x * moeda
    print("%d moeda(s) de R$ %.2f" % (x, moeda))
