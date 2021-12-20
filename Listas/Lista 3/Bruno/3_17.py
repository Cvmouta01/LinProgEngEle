numeros = []

for i in range(10):
    numeros.append(float(input(f'Insira o  {i+1}° numero real: ')))

for i in range(len(numeros)):
    if numeros[i] < 0:
        numeros[i] = 0

print(f'O vetor é: {numeros}')
