won_inter = 0
won_gremio = 0
draw = 0
matches = 0
winner = ''
do_again = True

while do_again:
    [goals_inter, goals_gremio] = [int(x) for x in input().split()]
    matches += 1

    if goals_inter > goals_gremio:
        won_inter += 1
    elif goals_gremio > goals_inter:
        won_gremio += 1
    else:
        draw += 1

    if won_inter > won_gremio:
        winner = 'Inter'
    elif won_gremio > won_inter:
        winner = 'Gremio'
    else:
        winner = 'Nao houve vencedor'
        
    
    user_response = int(input('Novo grenal (1-sim 2-nao)\n'))
    do_again = True if user_response == 1 else False

    if do_again == False:
        print('%d grenais' %matches)
        print('Inter:%d' %won_inter)
        print('Gremio:%d' %won_gremio)
        print('Empates:%d' %draw)
        print('%s venceu mais' %winner)
        

    
