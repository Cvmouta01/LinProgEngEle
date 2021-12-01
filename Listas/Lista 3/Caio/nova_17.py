numeros = list(map(float, input('Digite 10 números reais(separe-os com espaço): ').split()))

for i in range(len(numeros)):
    if numeros[i] < 0:
        numeros[i] = 0

print(f'Vetores: {numeros}')  # Não foi pedido o print mas acho que seria ideal né?
