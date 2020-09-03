grades = []

while True:
    test_grade = float(input())
    
    if test_grade < 0 or test_grade > 10:
        print('nota invalida')
    else:
        grades.append(test_grade)

        if len(grades) == 2:
            print('media = %.2f' %(sum(grades) / 2))
            break;
