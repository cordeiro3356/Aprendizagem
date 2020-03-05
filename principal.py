from fila import Fila
def main():
    filaTeste = Fila()
    filaTeste.inserirdados("ifpb")
    filaTeste.inserirdados("teste")
    filaTeste.inserirdados("valor final")
    print(filaTeste.getFila())
    filaTeste.removerDado()
    print(filaTeste.getFila())
    filaTeste.removev("teste")
    #remove o teste
    print(filaTeste.remove())
    #sai o primeiro valor
    print(filaTeste.TamanhoFila())
    #tamanho da fila



main()