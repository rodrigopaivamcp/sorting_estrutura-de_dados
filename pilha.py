class Pilha:
    def __init__(self):
        self.itens = []
    def empilhar(self, valor):
        self.itens.append(valor)
    def esta_vazia(self):
        return len(self.itens) == 0
    def desempilhar(self):
        if self.esta_vazia():
            raise IndexError("pilha vazia")
        return self.itens.pop()
    def topo(self):
        if self.esta_vazia():
            raise IndexError("pilha vazia")
        return self.itens[-1]
    def tamanho(self):
        return len(self.itens)