def divide(lis):
    neg = []
    pos = []
    for num in lis:
        if num < 0:
            neg.append(num)
        else:
            pos.append(num)
    return neg, pos


numeros = list(map(float, input('Digite 10 números reais(separe-os com espaço): ').split()))
negativos, positivos = divide(numeros)
print(f'Quantidade de números negativos: {len(negativos)}')
print(f'Soma dos números positivos: {sum(positivos)}')
