class Retangulo:
    #construtor
    def __init__(self,base,altura):
        #atributos
        self.ba = base
        self.al = altura

     #outros metodos
    def area (self):
        return (self.ba*self.al)
r1= Retangulo(10,2)