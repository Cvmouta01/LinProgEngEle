impares = []
restricao = []
numeros = []

for i in range(10):
    numeros.append(int(input(f'Insira o  {i+1}° numero inteiro: ')))

for num in numeros:
    if 0 <= num <= 50:
        restricao.append(num)

for num in restricao:
    if num % 2 == 1:
        impares.append(num)

print(impares)

for i in range(int(len(impares)/2)):
    print(f'{impares[2 * i]}, {impares[2 * i + 1]}')

if len(impares) % 2 == 1:
    print(impares[len(impares)-1])
