"""
Classes associam dados (atributos) e operações (metodos) em uma só estrutura

Um objeto é a uma variável cujo tipo é uma classe, ou seja, um objeito é uma instancia de uma classe


class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2

tv_quarto = Televisao()
tv_sala = Televisao()

print(tv_quarto.ligada)
print(tv_quarto.canal)

tv_sala.ligada = True
tv_sala.canal = 5

print(tv_sala.ligada)
print(tv_sala.canal)


Quando declaramos uma classe, estamos criando um novo tipo de dados

Da mesma forma que quando criamos uma lista ou uma string, estamos instanciando ou criando uma instancia
dessa classe

É a mesma coisa fazer lista = [] ou lista = list()

O método __init__ é chamado construtor e é chamado na criação do objeto

O parametro self significa o objeto televisão em si

self.ligada é um valor de self, ou seja, do objeto televisão

Sempre que criamos atributos do objeto, devemos associá-los a self

Caso contrário, se escrevessemos apenas ligada = False, ligada seria apenas uma variável local do métodos e não
atributo


"""

