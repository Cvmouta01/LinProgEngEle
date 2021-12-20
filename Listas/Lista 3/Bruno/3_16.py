numeros = []

for i in range(5):
    numeros.append(float(input(f'Insira o  {i+1}° numero real: ')))

codigo = int(input('Insira o codigo: '))

if codigo == 0:
    exit()

elif codigo == 1:
    print(f'O vetor é: {numeros}')

elif codigo == 2:
    numeros.reverse()
    print(f'O vetor invertido é: {numeros}')

else:
    print('Código inválido')
