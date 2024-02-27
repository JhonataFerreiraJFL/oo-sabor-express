from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import Item

class Restaurante:
    resturantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.resturantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f"{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}")
        for resturante in cls.resturantes:
            print(f'{resturante._nome.ljust(25)} | {resturante._categoria.ljust(25)} | {str(resturante.media_avaliacao).ljust(25)} |{resturante.ativo}')

    @property
    def ativo(self):
        return ' ⌧' if self._ativo else ' ☐'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
        
    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidades_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidades_de_notas, 1)
        return media
    
    #def adicionar_bebida_no_cardapio(self, bebida):
    #    self._cardapio.append(bebida)

    #def adcionar_prato_no_cardapio(self,prato):
    #    self._cardapio.append(prato)

    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio)
