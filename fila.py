class Fila:
    def __init__(self):
        self.itens = []
    def enfileirar(self, valor):
        self.itens.append(valor)
    def esta_vazia(self):
        return len(self.itens) == 0
    def desenfileirar(self):
        if self.esta_vazia():
            raise IndexError("fila vazia")
        return self.itens.pop(0)
    def frente (self):
        if self.esta_vazia():
            raise IndexError("fila vazia")
        return self.itens[0]
    def tamanho(self):
        return len(self.itens)
    