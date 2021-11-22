from math import log10

num = int(input('Digite um número inteiro: '))

if num < 0:
    print('Número inválido')
else:
    print(f'Logaritimo de {num}: {log10(num)}')
