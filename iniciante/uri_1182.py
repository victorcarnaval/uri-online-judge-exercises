idx_column = int(input())
operation = input()
matrix = []

for j in range(12):
    line = []

    for k in range(12):
        line.append(float(input()))

    matrix.append(line)

column = [line[idx_column] for line in matrix]

if operation == 'S':
    print('%.1f' %(sum(column)))
elif operation == 'M':
    print('%.1f' %(sum(column) / len(column)))
