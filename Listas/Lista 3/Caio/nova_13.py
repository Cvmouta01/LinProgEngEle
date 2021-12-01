numeros = list(map(float, input('Digite 5 números reais(separe-os com espaço): ').split()))
maior = max(numeros)
menor = min(numeros)

for pos in range(len(numeros)):
    if numeros[pos] == maior:
        posmaior = pos
    if numeros[pos] == menor:
        posmenor = pos

print(f'Posição do maior: {posmaior}\nPosição do menor: {posmenor}')
