class Restaurante:
    resturantes = []
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.resturantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        for resturante in Restaurante.resturantes:
            print(f'{resturante.nome} | {resturante.categoria} |{resturante.ativo}')

    @property
    def ativo(self):
        print(self)
        return 'verdadeiro' if self.ativo else 'false'
        

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiano')





Restaurante.listar_restaurantes()
