class Restaurante:
    resturantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.resturantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f"{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}")
        for resturante in cls.resturantes:
            print(f'{resturante._nome.ljust(25)} | {resturante._categoria.ljust(25)} |{resturante.ativo}')

    @property
    def ativo(self):
        return ' ⌧' if self._ativo else ' ☐'
    
    def alternar_estado(self):
        self._ativo = not self._ativo