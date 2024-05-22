class Cliente:
    def __init__(self, nome, anoNascimento, sexo, saldo, endereco, ativo):
        self.nome = nome
        self.anoNascimento = anoNascimento
        self.sexo = sexo
        self.saldo = saldo
        self.endereco = endereco
        self.ativo = ativo
        

    def imprimir(self):
        print("----------------------")
        print("nome:", self.nom e)
        print("anoNascimento:", self.anoNascimento)
        print("sexo:", self.sexo)
        print("saldo:", self.saldo)
        print("endereco:", self.endereco)
        print("ativo:", self.ativo)

    def verificaClienteAtivo(self):
            print("----------------------")
            if self.ativo == True:
                print("O cliente",self.nome, "Está ativo.")
            else:
                print("O cliente", self.nome, "Está inativo.")

    def calcularIdade(self):
            print("----------------------")
            anoAtual = 2024
            idade = (anoAtual - self.anoNascimento)
            print("A Idade do Cliente é", idade)

    def verificar_saldo(self):
            print("----------------------")
            if self.saldo >= 0 :
                print("O Saldo", self.saldo, "é positivo")
            else:
                print("O Saldo", self.saldo, "é negativo")
 

Cliente1 = Cliente("Luana", 2007, "F", 5000, "Rua teste", True)
Cliente2 = Cliente("Luana", 2007, "F", -5000, "Rua teste", True)
Cliente3 = Cliente("Luana", 2007, "F", 5000, "Rua teste", False)
Cliente1.imprimir()
Cliente2.imprimir()
Cliente3.imprimir()     

Cliente1.verificaClienteAtivo()
Cliente2.verificaClienteAtivo()
Cliente3.verificaClienteAtivo()

Cliente1.calcularIdade()
Cliente2.calcularIdade()
Cliente3.calcularIdade()

Cliente1.verificar_saldo()
Cliente2.verificar_saldo()
Cliente3.verificar_saldo()




class exercicio:
    def __init__(self):
        print('-')

    def exercicio1():
        print("resolução do exercicio")

ex = exercicio() 
ex.exercicio1()


