impares = []
numeros_limitados = []
numeros = list(map(int, input('Digite 10 números inteiros(separe-os com espaço): ').split()))

for num in numeros:
    if num >= 0 and num <= 50:
        numeros_limitados.append(num)

for num in numeros_limitados:
    if num % 2 == 1:
        impares.append(num)

if len(impares) % 2 == 1:
    impares.append('')
print(impares)
for i in range(int(len(impares)/2)):
    print(f'{impares[2 * i]}, {impares[2 * i + 1]}')
