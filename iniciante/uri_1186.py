operation = input()
matrix = []
total = 0
total_numbers = 0
i = 0

for j in range(12):
    line = []

    for k in range(12):
        line.append(float(input()))

    matrix.append(line)

idx = 1
idx_desc = 11

while i < len(matrix):
    if idx + 1 != idx_desc:
        total += sum(matrix[i][idx:])
        total_numbers += len(matrix[i][idx:])
        i += 1
        idx -= 1

if operation == 'S':
    print('%.1f' % total)
elif operation == 'M':
    print('%.1f' % (total / total_numbers))
