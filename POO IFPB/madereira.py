madeira1=20
madeira2=15
madeira3=40
desligar="ligar"
class Retangulo:
    def __init__(self, base: float, altura: float):
        self.__base = base
        self.__altura = altura

    @property
    def base(self):
        return self.__base

    @base.setter
    def base(self, novo_base: float):
        self.__base = novo_base

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, novo_altura: float):
        self.__altura = novo_altura

    def get_altura(self):
        return self.__altura

    def set_altura(self, novo:float):
        self.__altura = novo

    def get_base(self):
        return self.__base

    def set_base(self, novo_base:float):
        self.__base = novo_base

    def area(self):
        area=self.base * self.altura
        return area
    def perimetro(self):
        perimetro=self.base + self.altura
        return perimetro

while desligar != "desligar":
    print("para desligar o programa digite desligar! ")
    print("-"*50)
    print("madeira1 = 20R$ o m2, madeira2 = 15R$ o m2, madeira3 = 40R$ o m2 ")
    tipo=input("olá, informe o tipo de madeira (1,2 ou 3) ")
    valor=0
    if tipo == "desligar":
        break
    if tipo == "1":
        valor=20
    elif tipo == "2":
        valor = 15
    elif tipo == "3":
        valor = 40
    else:
        print("invalido")
    altura=float(input("informe a altura da moldura "))
    base=float(input("informe a base da moldura "))
    moldura=Retangulo(base,altura)
    print("|"*50)
    print ("a area da sua moldura é {} m2 seguido pelo perimetro de {} m e com o preço total de {}R$".format(moldura.area(),moldura.perimetro(),moldura.area()* int(valor)))
    print("-"*50)



