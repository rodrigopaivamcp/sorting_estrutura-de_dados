class Vetor:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.dados = [None] * capacidade
        self.quantidade = 0

    def esta_cheio(self):
        return self.quantidade == self.capacidade

    def esta_vazio(self):
        return self.quantidade == 0

    def exibir(self):
        print(self.dados[:self.quantidade])

    def obter(self, indice):
        if 0 <= indice < self.quantidade:
            return self.dados[indice]
        raise IndexError("indice invalido")

    def definir(self, indice, valor):
        if 0 <= indice < self.quantidade:
            self.dados[indice] = valor
        else:
            raise IndexError("indice invalido")

    def inserir(self, valor, posicao=None):
        if self.esta_cheio():
            raise OverflowError("vetor cheio")
        if posicao is None:
            posicao = self.quantidade
        for i in range(self.quantidade, posicao, -1):
            self.dados[i] = self.dados[i - 1]
        self.dados[posicao] = valor
        self.quantidade += 1

    def remover(self, posicao):
        if not (0 <= posicao < self.quantidade):
            raise IndexError("posicao invalida")
        valor_removido = self.dados[posicao]
        for i in range(posicao, self.quantidade - 1):
            self.dados[i] = self.dados[i + 1]
        self.dados[self.quantidade - 1] = None
        self.quantidade -= 1
        return valor_removido

    def buscar(self, valor):
        for i in range(self.quantidade):
            if self.dados[i] == valor:
                return i
        return -1