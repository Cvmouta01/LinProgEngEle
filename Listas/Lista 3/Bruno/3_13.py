numeros = []
for i in range(5):
    numeros.append(float(input(f'Insira o {i+1}º numero real: ')))

maior = max(numeros)
menor = min(numeros)
pmaior = []
pmenor = []

for pos in range(len(numeros)):
    if numeros[pos] == maior:
        pmaior.append(pos)
    if numeros[pos] == menor:
        pmenor.append(pos)

print(f'Posição do maior: {pmaior}\nPosição do menor: {pmenor}')
