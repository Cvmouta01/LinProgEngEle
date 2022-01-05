class Elevador:
    andar = 0
    pessoas = 0

    def __init__(self, capacidade, andares):
        self.capacidade = capacidade
        self.andares = andares

    def entra(self):
        if self.pessoas == self.capacidade:
            print(f'Não é possível entrar, a capacidade máxima é de {self.capacidade} pessoas.')
        else:
            self.pessoas += 1
            print(f'Agora temos {self.pessoas} pessoa(s) no elevador.')

    def sai(self):
        if self.pessoas == 0:
            print('Não há ninguem no elevador para sair.')
        else:
            self.pessoas -= 1
            print(f'Agora temos {self.pessoas} pessoa(s) no elevador.')

    def sobe(self):
        if self.andar == self.andares:
            print('\nEstamos no ultimo andar, não é possível subir.')
        else:
            self.andar += 1
            print(f'\nSubindo...\nChegamos no andar {self.andar}.')

    def desce(self):
        if self.andar == 0:
            print('\nEstamos no primeiro andar, não é possível descer.')
        else:
            self.andar -= 1
            print(f'\nDescendo...\nChegamos no andar {self.andar}.')

    def get_andar(self):
        return self.andar

    def get_pessoas(self):
        return self.pessoas

    def get_capacidade(self):
        return self.capacidade

    def get_andares(self):
        return self.andares

    def set_andar(self, novo):
        self.andar = novo

    def set_pessoas(self, novo):
        self.pessoas = novo

    def set_capacidade(self, novo):
        self.capacidade = novo

    def set_andares(self, novo):
        self.andares = novo


atlas = Elevador(5, 4)
atlas.entra()
atlas.entra()
atlas.entra()
atlas.entra()
atlas.entra()
atlas.entra()
atlas.entra()
atlas.sai()
atlas.sai()
atlas.sai()
atlas.sai()
atlas.sai()
atlas.sai()
atlas.sai()
atlas.sobe()
atlas.sobe()
atlas.sobe()
atlas.sobe()
atlas.sobe()
atlas.sobe()
atlas.desce()
atlas.desce()
atlas.desce()
atlas.desce()
atlas.desce()
atlas.desce()
print(f'\n{atlas.get_andar()}\n{atlas.get_pessoas()}\n{atlas.get_capacidade()}\n{atlas.get_andares()}')
atlas.set_andar(2)
atlas.set_pessoas(3)
atlas.set_capacidade(7)
atlas.set_andares(5)
print(f'\n{atlas.get_andar()}\n{atlas.get_pessoas()}\n{atlas.get_capacidade()}\n{atlas.get_andares()}')
