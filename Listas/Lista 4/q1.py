class Pessoa:

    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    def get_nome(self):
        return self.__nome

    def get_idade(self):
        return self.__idade

    def get_altura(self):
        return self.__altura

    def set_nome(self, novo):
        self.__nome = novo

    def set_idade(self, novo):
        self.__idade = novo

    def set_altura(self, novo):
        self.__altura = novo

    def show_data(self,):
        print(f'\nNome: {self.get_nome()}\nIdade: {self.get_idade()}\nAltura: {self.get_altura()}\n')


carlos = Pessoa('carlos', 17, 1.75)
carlos.show_data()
carlos.set_altura(1.76)
carlos.set_idade(18)
carlos.set_nome('carlão')
carlos.show_data()
