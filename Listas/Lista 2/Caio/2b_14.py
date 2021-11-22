n1, n2, n3 = map(float, input('Digite 3 notas(separe com espaço): ').split())
media = ((n1 * 2) + (n2 * 3) + (n3 * 5)) / 10

if media >= 5:
    print(f'Aprovado, media final: {media}')
elif media >= 3:
    print(f'Recuperação, media final: {media}')
else:
    print(f'reprovado, media final: {media}')
