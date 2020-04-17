class Motor:
    def __init__(self, velocidade=0):
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade = self.velocidade + 1

    def frear(self):
        self.velocidade = self.velocidade - 2
        self.velocidade = max(0, self.velocidade)
        #if self.velocidade <= 0:
        #    self.velocidade = 0
