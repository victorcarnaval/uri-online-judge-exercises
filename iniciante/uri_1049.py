first_word = input()
second_word = input()
third_word = input()

animals = {
    'vertebrado': {
        'ave': {
            'carnivoro': 'aguia',
            'onivoro': 'pomba'
            },
        'mamifero': {
            'onivoro': 'homem',
            'herbivoro': 'vaca'
            }
        },
    'invertebrado': {
        'inseto': {
            'hematofago': 'pulga',
            'herbivoro': 'lagarta'
            },
        'anelideo': {
            'hematofago': 'sanguessuga',
            'onivoro': 'minhoca'
            }
        }
    }

for first_key in animals:
    if first_key == first_word:
        for second_key in animals[first_key]:
            if second_key == second_word:
                for third_key in animals[first_key][second_key]:
                    if third_key == third_word:
                        print(animals[first_key][second_key][third_key])


