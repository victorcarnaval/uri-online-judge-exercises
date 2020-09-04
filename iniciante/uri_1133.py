n1 = int(input())
n2 = int(input())

if n1 > n2:
    n1, n2 = n2, n1

for x in range(n1 + 1, n2):
    if x % 5 == 2 or x % 5 == 3:
        print(x)
