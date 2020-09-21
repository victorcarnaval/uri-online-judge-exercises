vetor = []

for i in range(10):
    n = int(input())
    vetor.append(n)

for idx, val in enumerate(vetor):
    if val < 1:
        vetor[idx] = 1
    print('X[%d] = %d' %(idx, vetor[idx]))
    
