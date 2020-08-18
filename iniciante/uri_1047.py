[ini_hour, ini_min, end_hour, end_min] = [int(x) for x in input().split()]

if ini_hour >= end_hour and ini_min >= end_min:
    hour_duration = 24 - ini_hour + end_hour
else:
    hour_duration = end_hour - ini_hour

if ini_min > end_min:
    hour_duration -= 1
    min_duration = 60 - ini_min + end_min
else:
    min_duration = end_min - ini_min

print('O JOGO DUROU %d HORA(S) E %d MINUTO(S)' %(hour_duration, min_duration))
