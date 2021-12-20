op = input('soma = +\nsubtração = -\ndivisão = /\nmultiplicação = x\nEscolha uma das operações: ')
num1, num2 = map(float, input('Digite dois números: ').split())

if op == '+':
    print(f'soma dos números : {num1 + num2}')
elif op == '-':
    print(f'número 1 menos numero 2 : {num1 - num2}')
elif op == 'x':
    print(f'multiplicação dos números : {num1 * num2}')
elif op == '/':
    print(f'número 1 dividido pelo numero 2 : {num1 / num2}')
