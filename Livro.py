class Livro:
    def __init__(self):
        self.id = str()
        self.titulo = str()
        self.autor = str()

    def cadastrar(self):
        self.id = int(input("ID do Livro: "))
        self.titulo = str(input("Título do Livro: "))
        self.autor = str(input("Autor do livro: "))

    def imprime(self):
        print("Id:" ,self.id)
        print("Título:" ,self.titulo) 
        print ("Autor:" , self.autor)