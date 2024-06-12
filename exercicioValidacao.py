class Validacao:
    idade = None
    def __init__(self):
        pass

    def InserirNome(self,nome):
       nomePreenchido = self.ValidaNome(nome)
       if nomePreenchido == True:
           self.nome = nome
           print("Cadastrado com sucesso")

    def ValidaNome(self,nome):
        if len(nome)> 0 :
            print("O nome não pode estar vazio")   
            return False
        else:
            return True

    def InserirIdade(self,idade):
        idadeCorreta = self.ValidaIdade(idade)
        if idadeCorreta == True:
            self.idade = idade
            print("A idade precisa ser maior que 18")

    def ValidaIdade(self, idade):
        if idade > 18:
            print("Valor cadastrado com sucesso")   
            return False
        else:
            return True    
        
    def Inserirsaldo(self,saldo):
        saldoCorreto = self.ValidaSaldo(saldo)
        if  saldoCorreto == True:
            self.saldo = saldo
            print("Valor cadastrado com sucesso")

    def ValidaSaldo(self, saldo):
        if saldo < 0:
            print("O Saldo precisa ser maior que 0")   
            return False
        else:
            return True

cad = Cadastro()
cad.InsrirNome(Luana)
cad. InserirIdade(17)
cad. InserirSaldo(100)


