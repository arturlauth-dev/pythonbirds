class Direcao:
    def __init__(self, auxdirecao = 0):
        self.map = {0: 'Norte', 1: 'Leste', 2: 'Sul', 3: 'Oeste'}
        self.auxdirecao = auxdirecao
        self.valor = self.map[self.auxdirecao]

    def girar_a_direita(self):
        self.auxdirecao +=1
        if self.auxdirecao == 4:
            self.auxdirecao = 0
        self.valor = self.map[self.auxdirecao]

    def girar_a_esquerda(self):
        self.auxdirecao -=1
        if self.auxdirecao == -1:
            self.auxdirecao = 3
        self.valor = self.map[self.auxdirecao]