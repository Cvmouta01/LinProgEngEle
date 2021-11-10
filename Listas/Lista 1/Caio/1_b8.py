n1, n2 = map(float, input('Digite as notas(separe com espaço): ').split())
if 0 <= n1 <= 10 and 0 <= n2 <= 10:
    print(f'Média: {(n1 + n2)/2}')
else:
    print('Alguma(s) nota(s) não é(são) valida(s)')
