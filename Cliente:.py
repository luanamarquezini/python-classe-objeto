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
        print("nome:", self.nome)
        print("anoNascimento:", self.anoNascimento)
        print("sexo:", self.sexo)
        print("saldo:", self.saldo)
        print("endereco:", self.endereco)
        print("ativo:", self.ativo)

        def verificaClienteAtivo(self):
            if self.ativo == True:
                print("O cliente",self.nome, "Está ativo.")
            else:
                print("O cliente", self.nome, "Está inativo.")

Cliente1 = Cliente("Luana", 2007, "F", 5000, "Rua teste", True)
Cliente2 = Cliente("Luana", 2007, "F", -5000, "Rua teste", True)
Cliente3 = Cliente("Luana", 2007, "F", 5000, "Rua teste", False)
Cliente1.imprimir()
Cliente2.imprimir()
Cliente3.imprimir()     

Cliente1.verificaClienteAtivo()
Cliente2.verificaClienteAtivo()
Cliente3.verificaClienteAtivo()

