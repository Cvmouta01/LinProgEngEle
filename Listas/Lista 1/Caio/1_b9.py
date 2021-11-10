sal, pr = map(float, input('Salário e prestação(separe com espaço): ').split())
if pr > sal * 0.2:
    print('Empréstimo não concedido')
else:
    print('Empréstimo concedido')
