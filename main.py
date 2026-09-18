from vetor import Vetor
from lista_simples import ListaEncadeada
from lista_dupla import ListaDuplamenteEncadeada
from lista_circular import ListaCircular

vetor = Vetor(5)
vetor.inserir(10)
vetor.inserir(20)
vetor.inserir(30)
vetor.exibir()
print("Busca:", vetor.buscar(20))
vetor.remover(1)
vetor.exibir()