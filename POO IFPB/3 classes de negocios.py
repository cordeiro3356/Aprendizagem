class computador:
    def __init__(self, marca: str, preço: float, cpu: str):
        self.cpu = cpu
        self.preço = preço
        self.marca = marca
class software:
    def __init__(self, função: str, tamanho: str, preço: float):
        self.função = função
        self.tamanho = tamanho
        self.preço = preço
class funcionario:
    def __init__(self, idade:str, salario: float, função:str):
        self.idade = idade
        self.salario = salario
        self.função = função

Jorge = funcionario(22,1400,"suporte de TI")
Irineu = funcionario(34,3500,"analista de redes")
Windows = software("Sistema operacional", "10 GB",200)
pc1 = computador("dell",2500,"i5")
print(pc1.cpu)
print(Windows.função)
print(Jorge.salario)
print(Irineu.função)

