class ListaEncadeada:
    def __init__(self):
        self.cabeca = None
        self.tamanho = 0

    def inserir_fim(self, valor):
        novo = No(valor)
        if self.cabeca is None:
            self.cabeca = novo
        else:
            atual = self.cabeca
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo
        self.tamanho += 1

    def remover(self, valor):
        anterior = None
        atual = self.cabeca
        while atual is not None:
            if atual.valor == valor:
                if anterior is None:
                    self.cabeca = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                self.tamanho -= 1
                return True
            anterior = atual
            atual = atual.proximo
        return False

    def buscar(self, valor):
        atual = self.cabeca
        indice = 0
        while atual is not None:
            if atual.valor == valor:
                return indice
            atual = atual.proximo
            indice += 1
        return -1

    def exibir(self):
        atual = self.cabeca
        valores = []
        while atual is not None:
            valores.append(atual.valor)
            atual = atual.proximo
        print(valores)