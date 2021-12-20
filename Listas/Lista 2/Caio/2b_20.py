l1, l2, l3 = map(float, input('Digite os três lados de um triângulo: ').split())
if l1 + l2 > l3 and l2 + l3 > l1 and l3 + l1 > l2:

    if l1 == l2 and l2 == l3:
        print('É um triângulo equilátero')

    elif l1 == l2 or l2 == l3:
        print('É um triângulo isósceles')

    else:
        print('É um triângulo escaleno')
