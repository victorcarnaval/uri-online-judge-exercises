numbers = []

for x in range(1, 7):
    numbers.append(float(input()))

positives = 0
for x in numbers:
    if x >= 0:
        positives += 1

print('%d valores positivos' %positives)
