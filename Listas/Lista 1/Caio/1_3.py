inteiros = []
nums = input('Digite 3 números inteiros(separe com espaços)').split()
for num in nums:
    inteiros.append(int(num))
print(f'Soma: {sum(inteiros)}')
