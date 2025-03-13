# Exercício 2 - Revisão sobre classes

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def falar(self):
        print(f'seu nome é {self.nome}')

    @property
    def mostra_idade(self):
        return self.nome

    @mostra_idade.setter
    def mostra_idade(self, nome):
        self.nome = nome

yago = Pessoa('yago', 19)
# nome = yago.falar()
# nome = yago.mostra_idade

print(yago.mostra_idade)