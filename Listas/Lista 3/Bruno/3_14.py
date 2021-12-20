numeros = []
repetidos = []

for i in range(10):
    numeros.append(float(input(f'Insira o {i+1}º valor: ')))

for j in range(len(numeros)):
    for k in range(len(numeros)):
        if j != k:
            if numeros[j] == numeros[k] and numeros[j] not in repetidos:
                repetidos.append(numeros[j])

print(f'Os valores repetidos são: {repetidos}')
