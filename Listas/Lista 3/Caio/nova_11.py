def divide(lis):
    neg = []
    pos = []
    for num in lis:
        if num < 0:
            neg.append(num)
        else:
            pos.append(num)
    return neg, pos


numeros = [1, 2, 3, 4, 5.3, -1, -2, -3, -4, -5.3]
negativos, positivos = divide(numeros)
print(f'Quantidade de números negativos: {len(negativos)}')
print(f'Soma dos números positivos: {sum(positivos)}')
