n1 = int(input())
n2 = int(input())
total_sum = 0

if n1 > n2:
    n1, n2 = n2, n1

for x in range(n1, n2 + 1):
    if x % 13 != 0:
        total_sum += x

print(total_sum)
