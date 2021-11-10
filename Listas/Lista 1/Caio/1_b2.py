num = float(input('Digite um número real:'))
if num < 0:
    print(f'O número {num} é negativo e não possui raiz real, o número é invalido')
else:
    print(f'A raiz de {num} é {num**0.5}')
