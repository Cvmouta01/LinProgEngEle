altura = float(input('Digite sua altura: '))
sexo = input('Insira o seu sexo(m ou f): ')
if sexo == 'm':
    print(f'Peso ideal: {72.7 * altura - 58}')
if sexo == 'f':
    print(f'Peso ideal: {62.1 * altura - 44.7}')
