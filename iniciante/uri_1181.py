idx_line = int(input())
operation = input()
matrix = []

for j in range(12):
    line = []

    for k in range(12):
        value = float(input())
        line.append(value)

    matrix.append(line)

target_line = matrix[idx_line]

if operation == 'S':    
    result = sum(target_line)
elif operation == 'M':
    result = sum(target_line) / len(target_line)

print('%.1f' % result)
    
