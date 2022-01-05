class Agenda:

    def __init__(self):
        self.lista = []

    def armazena_pessoa(self, nome, idade, altura):
        self.lista.append({'nome': nome, 'idade': idade, 'altura': altura})

    def remove_pessoa(self, pessoa):
        for person in self.lista:
            if person['nome'] == pessoa:
                self.lista.remove(person)

    def imprime_agenda(self):
        i = 0
        for person in self.lista:
            print(f'\nPessoa {i}:')
            print(f'nome: {person["nome"]}\nidade: {person["idade"]}'
            f'\naltura: {person["altura"]}')
            i += 1

    def busca_pessoa(self, nome):
        i = 0
        for person in self.lista:
            if person['nome'] == nome:
                print(f'\n\nA pessoa está na posição {i}')
            i += 1

    def imprime_pessoa(self, index):
        print(f'\nnome: {self.lista[index]["nome"]}'
        f'\nidade: {self.lista[index]["idade"]}'
        f'\naltura: {self.lista[index]["altura"]}')


ag = Agenda()
ag.armazena_pessoa('meiga', 19, 1.79)
ag.armazena_pessoa('ponce', 19, 1.70)
ag.armazena_pessoa('maio', 20, 1.74)
ag.imprime_agenda()
ag.remove_pessoa('ponce')
print('\nApós a retirada do ponce')
ag.imprime_agenda()
ag.busca_pessoa('maio')
ag.imprime_pessoa(1)
