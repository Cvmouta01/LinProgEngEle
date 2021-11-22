base1 = float(input('Digite a base do trapezio: '))
base2 = float(input('Digite a outra base do trapezio: '))
altura = float(input('Digite a altura do trapezio:'))

if base1 < 0 or base2 < 0 or altura < 0:
    print('Número inválido')
else:
    print(f'Área: {((base1 + base2) * altura) /2}')
