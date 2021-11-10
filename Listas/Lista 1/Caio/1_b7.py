n1, n2 = map(float, input('Dois números (separe com espaço): ').split())
if n1 == n2:
    print('Os numeros são iguais')
else:
    print(f'{max(n1,n2)} é o maior número')
