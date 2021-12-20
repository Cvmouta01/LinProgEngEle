def media(lista):
    soma = 0
    for num in lista:
        soma += num

    return soma / len(lista)


numeros = list(map(float, input('Digite 5 números reais(separe-os com espaço): ').split()))
print(f'Números: {numeros}')
print(f'Maior: {max(numeros)}\nMenor: {min(numeros)}')
print(f'Média: {media(numeros)}')
