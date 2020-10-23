operation = input()
matrix = []
total = 0
total_numbers = 0

for j in range(12):
    line = []

    for k in range(12):
        line.append(float(input()))

    matrix.append(line)

matrix_length = len(matrix)
i = 0
idx_final = matrix_length

while i < matrix_length:
    if i >= (matrix_length / 2):
        total += sum(matrix[i][idx_final:i])
        total_numbers += len(matrix[i][idx_final:i])
    i += 1
    idx_final -= 1

if operation == 'S':
    print('%.1f' % total)
elif operation == 'M':
    print('%.1f' % (total / total_numbers))
