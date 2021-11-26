def razao(mat):
    for i in range(len(mat)):
        dens = mat[i][2] / mat[i][1]
        matriz[i].append(dens)


def printa_mat(mat):
    print('num   volume     preço     razão')
    for lis in mat:
        print('%s:   %f   %0.2f    %0.1f' % (lis[0], lis[1], lis[2], lis[3]))
    print('\n')


def ordena(mat):
    lista = []
    for lis in mat:
        lista.append(lis[3])
    lista.sort()
    lista.reverse()
    return lista


def reordena_matriz(mat, raz):
    nova_lista = []
    for num in raz:
        for lis in mat:
            if num == lis[3]:
                nova_lista.append(lis)
                break
    return nova_lista


def enche_bau(mat):
    caminhao = []
    volume_total = 3
    for lis in mat:
        if lis[1] <= volume_total:
            volume_total -= lis[1]
            caminhao.append(lis)
    return caminhao


def produtos(mat, tra):
    produtos = []
    for lis in mat:
        for tupla in tra:
            if lis[0] == tupla[0]:
                produtos.append(tupla[1])
                break
    for produto in produtos:
        print(produto)


matriz = [
['01', 0.751, 999.90],
['02', 0.0035, 2499.90],
['03', 0.0319, 299.29],
['04', 0.527, 3999.90],
['05', 0.000089, 2199.12],
['06', 0.496, 199.9],
['07', 0.635, 849.00],
['08', 0.400, 4346.99],
['09', 0.290, 3999.90],
['10', 0.200, 2999.90],
['11', 0.498, 1999.90],
['12', 0.0544, 429.90],
['13', 0.0424, 429.90],
['14', 0.870, 1199.98]]
# Cada linha da da matriz representa um produto e possui número identificador, volume e valor respectivo ao produto.

traducao = [['01', 'Geladeira'],
['02', 'Notebook Dell'],
['03', 'Microondas X'],
['04', 'Notebook ASUS'],
['05', 'IPhone 8'],
['06', 'Ventilador Gelado'],
['07', 'Freezer'],
['08', "TV 55'"],
['09', "TV 50'"],
['10', "TV 42'"],
['11', 'Notebook Lenovo'],
['12', 'Microondas Y'],
['13', 'Microondas Z'],
['14', 'Geladeira faz frio']]

razao(matriz)
print('\nMatriz: \n')
printa_mat(matriz)
razoes = ordena(matriz)
matriz = reordena_matriz(matriz, razoes)
print('Matriz ordenada pela razão: \n')
printa_mat(matriz)
caixote = enche_bau(matriz)
print('Matriz dos produtos suportados no caminhão baú:\n')
printa_mat(caixote)
print('Itens a serem tranportados:\n')
produtos(caixote, traducao)
