solos = []
numeros = list(map(float, input('Digite 20 números reais(separe-os com espaço): ').split()))

for num in numeros:
    if num not in solos:
        solos.append(num)
print(f"Números : {solos}")
