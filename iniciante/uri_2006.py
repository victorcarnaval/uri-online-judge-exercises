tea = input()
guesses = input().split(' ')
acc = 0

for guess in guesses:
    if guess == tea:
        acc += 1

print(acc)
