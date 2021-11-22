soma = 0
num = input('Digite um número inteiro positivo: ')

if int(num) <= 0:
    print('Número inválido')

else:
    for algarismo in num:
        soma += int(algarismo)
    print(soma)
