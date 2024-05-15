class Veiculo:
    def _init_(self,marca,modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def ligar(self):
        print("Veículo ligado")

    def desligar(self):
        print("Veículo desligado")   

class Carro(Veiculo):
    def _init_(self,marca,modelo,ano,numeroDePortas):   
        super()._init_(marca,modelo,ano)
        self.numeroDePortas = numeroDePortas

    def NumeroDePortas(self):
        print("O Carro posui: ", self.numeroDePortas)

class Moto(Veiculo):
    def _init_(self,marca,modelo,ano,cilindradas):   
        super()._init_(marca,modelo,ano)
        self.cilindradas = cilindradas

    def Cilindradas(self):
        print("A Moto posui: ", self.cilindradas)
 
veiculo = Veiculo("Toyota, Corolla, 2024, 4")
carro = Carro("Chevrolet, Tracker, 2022, 4")
moto = Moto("Honda, Twister, 2024, 293,5")

    

veiculo.imprimir()
carro.imprimir()
moto.imprimir()
