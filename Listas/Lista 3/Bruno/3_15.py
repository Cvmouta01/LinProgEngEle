numeros = []
solos = []

for i in range(20):
    numeros.append(int(input(f'Insira o {i+1}º numero inteiro: ')))

for num in numeros:
    if num not in solos:
        solos.append(num)

print(f'Retirando os valores repetidos temos: {solos}')
