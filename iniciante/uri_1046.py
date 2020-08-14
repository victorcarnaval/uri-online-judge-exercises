[initial_hour, final_hour] = [int(x) for x in input().split()]

hours_left = 24 - initial_hour

if initial_hour >= final_hour:
    hours_left += final_hour
else:
    hours_left -= 24 - final_hour

print('O JOGO DUROU %d HORA(S)' % hours_left)

