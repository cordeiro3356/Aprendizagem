from Fila import Fila

Estacionamento = Fila()
def main():
    continuar=1
    remover=1
    mostrar=str
    while continuar>0:
        Estacionamento.inserirDado(input('Digite a placa do carro que entrará: '))
        continuar=int(input("digite 0 para parar o programa. Para continuar inserindo digite 1"))
        mostrar=input(" digite a letra s para mostrar o estado do estacionamento")
        if mostrar=="s" or mostrar=="S" or mostrar=="":
            print(Estacionamento.getFila())
        remover = int(input("deseja remover algum carro? 1 para sim 0 para não"))
        if remover==1:
            while remover==1:
                Estacionamento.removerFila(input('Digite a placa do carro que irá sair: '))
                print(Estacionamento.getFila())
                remover=int(input("digite o valor 0 para parar de remover ou digite 1 para continuar removendo"))
    print("Fim do programa!")

main()
