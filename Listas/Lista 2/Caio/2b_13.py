n1, n2, n3 = map(float, input('Digite 3 notas(separe com espaço): ').split())
media = (n1 + n2 + (n3 * 2)) / 4

if media >= 60:
    print(f'Aprovado, media final: {media}')
else:
    print(f'Reprovado, media final: {media}')
