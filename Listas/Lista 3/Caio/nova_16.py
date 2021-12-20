numeros = list(map(float, input('Digite 5 números reais(separe-os com espaço): ').split()))
codigo = int(input('Insira o código: '))

if codigo == 0:
    exit()

elif codigo == 1:
    print(f'vetor: {numeros}')

elif codigo == 2:
    numeros.reverse()
    print(f'vetor invertido: {numeros}')

else:
    print('Código inválido')
