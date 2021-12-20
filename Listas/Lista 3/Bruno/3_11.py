def organiza(lis):
    pos = []
    neg = []
    for num in lis:
        if num < 0:
            neg.append(num)
        else:
            pos.append(num)
    return neg, pos


numeros = []
for i in range(10):
    numeros.append(float(input(f'Insira o {i+1}º numero real: ')))

negativo, positivo = organiza(numeros)
print(f'A quantidade de numeros negativos é {len(negativo)}')
print(f'A soma dos numeros positivos é {sum(positivo)}')
