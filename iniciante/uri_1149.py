x = list(map(int, input().split()))
i = 1

while x[i] <= 0:
    if x[i] <= 0:
        i += 1
    else:
        break

total_sum = 0
for j in range(0, x[i]):
    total_sum += x[0] + j

print(total_sum)
