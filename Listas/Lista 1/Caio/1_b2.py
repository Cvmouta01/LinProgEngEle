num = float(input('Digite um numero real:'))
if num < 0:
    print(f'O numero {num} é negativo e não possui raiz, o número é invalido')
else:
    print(f'A raiz de {num} é {num**0.5}')
