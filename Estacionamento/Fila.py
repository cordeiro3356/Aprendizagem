class Fila:

    def __init__(self):
        self.dados = []

    def getFila(self):
        return self.dados

    def inserirDado(self, novoValor):
        self.dados.append(novoValor)

    def removerDado(self, valor):
        pos = self.dados.index(valor)
        for i in range(0, pos + 1):
            self.dados.pop(0)

    def removerFila(self, valor):
        pos = self.dados.index(valor)
        tam = len(self.dados)
        for i in range(len(self.dados)):
            if self.dados[i] != valor:
                self.dados.append(self.dados[i])
        for i in range(tam):
            self.dados.pop(0)
