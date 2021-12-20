numeros = []
multiplos = []
x = int(input('Digite um valor para x: '))

for i in range(10):
    numeros.append(float(input(f'Insira o  {i+1}° numero real: ')))

for num in numeros:
    if num % x == 0:
        multiplos.append(num)

print(f'Os multiplos de {x} são: {multiplos}')
