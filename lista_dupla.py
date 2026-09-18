class ListaDuplamenteEncadeada:
    def __init__(self):
        self.cabeca = None
        self.cauda = None
        self.tamanho = 0

    def inserir_fim(self, valor):
        novo = NoDuplo(valor)
        if self.cabeca is None:
            self.cabeca = novo
            self.cauda = novo
        else:
            novo.anterior = self.cauda
            self.cauda.proximo = novo
            self.cauda = novo
        self.tamanho += 1

    def remover(self, valor):
        atual = self.cabeca
        while atual is not None:
            if atual.valor == valor:
                if atual.anterior is not None:
                    atual.anterior.proximo = atual.proximo
                else:
                    self.cabeca = atual.proximo
                
                if atual.proximo is not None:
                    atual.proximo.anterior = atual.anterior
                else:
                    self.cauda = atual.anterior
                
                self.tamanho -= 1
                return True
            atual = atual.proximo
        return False

    def exibir_do_inicio(self):
        atual = self.cabeca
        valores = []
        while atual is not None:
            valores.append(atual.valor)
            atual = atual.proximo
        print(valores)

    def exibir_do_fim(self):
        atual = self.cauda
        valores = []
        while atual is not None:
            valores.append(atual.valor)
            atual = atual.anterior
        print(valores)