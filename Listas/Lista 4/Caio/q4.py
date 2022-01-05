# Não pede botão de ligar/desligar, mas eu adicionei para ter a consciência limpa
class Televisão:
    ligada = False
    volume = 0
    canal = 0

    def __init__(self):
        pass

    def get_ligada(self):
        return self.ligada

    def get_volume(self):
        return self.volume

    def get_canal(self):
        return self.canal

    def liga_desliga(self):
        if self.ligada is True:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_volume(self):
        if self.ligada is True:
            self.volume += 1
        else:
            print('A a Tv está desligada, aperte o botão self.liga_desliga() para ligar a Televisão')

    def abaixa_volume(self):
        if self.ligada is True:
            self.volume -= 1
        else:
            print('A a Tv está desligada, aperte o botão self.liga_desliga() para ligar a Televisão')

    def aumenta_canal(self):
        if self.ligada is True:
            self.canal += 1
        else:
            print('A a Tv está desligada, aperte o botão self.liga_desliga() para ligar a Televisão')

    def abaixa_canal(self):
        if self.ligada is True:
            self.canal -= 1
        else:
            print('A a Tv está desligada, aperte o botão self.liga_desliga() para ligar a Televisão')

    def set_canal(self, novo):
        self.canal = novo


class ControleRemoto:
    
    def __init__(self):
        pass

    def volume_mais(self, tv):
        tv.aumenta_volume()

    def volume_menos(self, tv):
        tv.abaixa_volume()

    def canal_mais(self, tv):
        tv.aumenta_canal()

    def canal_menos(self, tv):
        tv.abaixa_canal()

    def liga_desliga(self, tv):
        tv.liga_desliga()


lg = Televisão()
epson = ControleRemoto()
epson.canal_mais(lg)
print(lg.get_ligada())
epson.liga_desliga(lg)
print(lg.get_ligada())
print(lg.get_canal())
print(lg.get_volume())
epson.canal_mais(lg)
epson.canal_mais(lg)
epson.volume_mais(lg)
epson.volume_mais(lg)
print(lg.get_canal())
print(lg.get_volume())
epson.volume_menos(lg)
epson.canal_menos(lg)
print(lg.get_canal())
print(lg.get_volume())
epson.liga_desliga(lg)
epson.volume_menos(lg)
epson.canal_mais(lg)
