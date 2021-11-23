num = int(input('Digite um número inteiro: '))

if num % 3 == 0 and num % 5 != 0:
    print(f'O número {num} é divisível por 3')
elif num % 3 != 0 and num % 5 == 0:
    print(f'O número {num} é divisível por 5')
