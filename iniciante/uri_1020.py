days = int(input())

years = days / 365
days = days % 365
months = days / 30
days = days % 30

print("%d ano(s)\n%d mes(es)\n%d dia(s)" % (years, months, days))
