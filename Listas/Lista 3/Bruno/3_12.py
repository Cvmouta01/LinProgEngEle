def media(lis):
    soma = 0
    for num in lis:
        soma += num

    return soma / len(lis)


numeros = []

for i in range(5):
    numeros.append(float(input(f'Insira o {i+1}º valor: ')))

print(f'Os valores lidos são: {numeros}')
print(f'O maior valor é {max(numeros)}\n O menor valor é {min(numeros)}')
print(f'A media dos valores é {media(numeros)}')
