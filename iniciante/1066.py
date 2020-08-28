numbers = []
even_num = 0
odd_num = 0
positive_num = 0
negative_num = 0

x = 5
while x > 0:
    number = int(input())
    if number % 2 == 0:
        even_num += 1
    else:
        odd_num += 1

    if number > 0:
        positive_num += 1
    elif number < 0:
        negative_num += 1
        
    x -=1
    
print('%d valor(es) par(es)' % even_num)
print('%d valor(es) impar(es)' % odd_num)
print('%d valor(es) positivo(s)' % positive_num)
print('%d valor(es) negativo(s)' % negative_num)
