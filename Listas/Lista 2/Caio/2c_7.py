numeros = list(map(int, input('Digite 10 números inteiros: ').split()))
numerosfinal = []

for num in numeros:
    if num >= 0:
        numerosfinal.append(num)
print(f"Média: {sum(numerosfinal)/len(numerosfinal)}")
