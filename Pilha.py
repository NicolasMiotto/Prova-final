from No import No

class Pilha:

	def __init__(self):
		self.cima = None
		self.tamanho = 0

	def add(self, valor):
		no = No( valor )
		if self.tamanho == 0 :
			self.cima = no
		else: 
			no.proximo = self.cima
			self.cima = no
		self.tamanho +=1

	def imprime(self):
		if self.tamanho == 0:
			print( "Vazio!" )
		else:
			aux = self.cima
			while( aux ) :
				print( aux.dado )
				aux = aux.proximo
			print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

	def excluir(self):
		if self.tamanho == 0:
			print( "Vazio!" )
		elif self.tamanho == 1:
			self.cima = None
			self.tamanho = 0
		else:
			self.cima = self.cima.proximo
			self.tamanho -= 1
		self.imprime()    
