from fila import Fila
from pilha import Pilha 

fila = Fila()

fila.enfileirar(10)
fila.enfileirar(20)
fila.enfileirar(30)

print(fila.frente())       
print(fila.desenfileirar())
print(fila.tamanho()) 


from pilha import Pilha

pilha = Pilha()

pilha.empilhar(10)
pilha.empilhar(20)
pilha.empilhar(30)

print(pilha.topo())       
print(pilha.desempilhar()) 
print(pilha.topo())        
print(pilha.tamanho())    

