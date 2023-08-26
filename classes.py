class Pessoa:
    def __init__(self, a, b):
        self.nome = a
        self.idade = b

    def apresentar(self):
        print(f'Meu nome é {self.nome} e tenho {self.idade} anos!')

pessoa1 = Pessoa("zezinho", 10)
pessoa2 = Pessoa("joaozinho", 15)

x = 'teste'

pessoa1.apresentar()
pessoa2.apresentar()


