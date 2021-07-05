from Pilha import Pilha
from Livro import Livro


pilha = Pilha()

pilha.imprime()

pilha.add("Bíblia Sagrada")
pilha.add("Harry Potter")
pilha.add("O capital")
pilha.imprime()



pilha.add("O Manifesto ágil")
pilha.add("A arte sutil de não ligar o foda-se")
pilha.add("Guerra dos tronos")


pilha.imprime()


print("----- Remoção de itens ------")

pilha.excluir()
pilha.imprime()

pilha.excluir()
pilha.excluir()
pilha.excluir()
pilha.excluir()
pilha.excluir()

pilha.imprime()