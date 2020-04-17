class Pessoa:
    olhos = 2 #atributo default
    def __init__(self, *filhos, nome=None, idade=35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @staticmethod #decorator
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos{cls.olhos}'

class Homem(Pessoa):
    def cumprimentar(self):
        #cumprimentar_da_classe_pai = Pessoa.cumprimentar(self)
        cumprimentar_da_classe_pai = super().cumprimentar()
        return f'{cumprimentar_da_classe_pai} .Aperto de mão'

class Mutante(Pessoa):
    olhos = 3

if __name__ == '__main__':
    renzo = Mutante(nome='Renzo')
    luciano = Homem(renzo, nome='Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print (f'{filho.nome} +')
    luciano.sobrenome = 'Ramalho' #esse tipo de ação
    del luciano.filhos              #deve ser evitado
    luciano.olhos = 1
    del luciano.olhos
    print(luciano.__dict__)
    print(renzo.__dict__)
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(renzo.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(renzo.olhos))
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), luciano.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(renzo, Pessoa))
    print(isinstance(renzo, Homem))
    print(isinstance(renzo, Pessoa))
    print(isinstance(renzo, Homem))
    print(renzo.olhos)
    print(renzo.cumprimentar())
    print(luciano.cumprimentar())