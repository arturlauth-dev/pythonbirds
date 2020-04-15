class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo')
    artur = Pessoa(nome='Artur')
    luciano = Pessoa(renzo,artur, nome='Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print (f'{filho.nome} +')
    luciano.sobrenome = 'Ramalho' #esse tipo de ação
    del luciano.filhos              #deve ser evitado
    print(luciano.__dict__)
    print(renzo.__dict__)
