x = int(input())
y = int(input())

if x > y:
    x, y = y, x

odd_sum = 0

for j in range(x + 1, y):
    if j % 2 != 0:
        odd_sum += j

print(odd_sum)
