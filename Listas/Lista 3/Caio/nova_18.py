multiplos = []
numeros = list(map(float, input('Digite 10 números reais(separe-os com espaço): ').split()))
x = int(input('Digite um número inteiro: '))
for num in numeros:
    if num % x == 0:
        multiplos.append(num)
print(f'Multiplos de {x}: {multiplos}')
