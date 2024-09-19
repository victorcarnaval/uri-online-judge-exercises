operation = input()
matrix = []
total = 0
total_numbers = 0

for j in range(12):
    line = []

    for k in range(12):
        line.append(float(input()))

    matrix.append(line)

i = 0
j = 0
total = 0
total_numbers = 0

while i < len(matrix):
    if i == 0:
        j = 12
    elif i < 6:
        j = -i
    else:
        j = i + 1

    total += sum(matrix[i][j:])
    total_numbers += len(matrix[i][j:])
    i+= 1

if operation == 'S':
    print('%.1f' % total)
elif operation == 'M':
    print('%.1f' % (total / total_numbers))
