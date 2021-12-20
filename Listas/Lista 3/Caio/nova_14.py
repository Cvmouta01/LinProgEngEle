repetidos = []
numeros = list(map(float, input('Digite 10 números reais(separe-os com espaço): ').split()))
for i in range(len(numeros)):
    numteste = numeros[0]
    numeros.remove(numeros[0])
    for numero in numeros:
        if numero == numteste and numero not in repetidos:
            repetidos.append(numero)

print(f"Números repetidos: {repetidos}")
