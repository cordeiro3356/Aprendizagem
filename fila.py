class Fila:
    def __init__(self):
        self.dados=[]
    def getFila(self):
        return self.dados
    def removerDado(self):
        return self.dados.pop(0)
    def inserirdados(self,novovalor):
        return self.dados.append(novovalor)
    def remove(self):
        return self.dados.pop(0)
    def removev(self,valor):
        pos=self.dados.index(valor)
        for i in range(0,pos+1):
            self.dados.pop(0)
    def TamanhoFila(self):
        return len(self.dados)
