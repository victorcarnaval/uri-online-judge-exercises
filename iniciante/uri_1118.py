def request_grade():
    while True:
        n = float(input())

        if n < 0 or n > 10:
            print('nota invalida')
            continue
        break
    return n

def do_again():
    
    while True:
        user_response = int(input('novo calculo (1-sim 2-nao)\n'))

        if user_response != 1 and user_response != 2:
            continue
    
        user_response = True if user_response == 1 else False
        break
    return user_response

while True:
    n1 = request_grade()
    n2 = request_grade()

    print('media = %.2f' %((n1 + n2) / 2))

    if do_again() == False:
        break
    
    
