###Função Para calcular a taxa metabólica basal (TMB).
def TMB (kg,gp):
    codigo=[1,2,3,4,5]
    constante=[129,78,70,49,10]
    nome=["passeriformes","não passeriformes","mamiferos placentarios","masurpiais e endetatas","répteis"]
    c=gp
    k=constante[c-1]
    tmb=(kg**0.75)*k
    return tmb
###Função Para calcular a taxa metabólica específica (TME).
def TME (kg,gp):
    codigo=[1,2,3,4,5]
    constante=[129,78,70,49,10]
    nome=["passeriformes","não passeriformes","mamiferos placentarios","masurpiais e endetatas","répteis"]
    c=gp
    k=constante[c-1]
    tme=(kg**0.25)*k
    return tme
###Função main
def main():
    kg=int(input("digite o kg do animal"))
    nome = [" 1 passeriformes", "2 não passeriformes", "3 mamiferos placentarios", "4 masurpiais e endetatas", "5 répteis"]
    print(nome)
    gp=int(input("digite o codigo do grupo do animal  "))
    letra = str(input("digite a flag B ou E"))
    if letra=="B" or letra=="b":
        print("o PMV é {:.2f}".format(TMB(kg,gp)))
    elif letra=="E" or letra=="e":
        print("o PME é {:.2f}".format(TME(kg, gp)))
    else:
        print(" flag invalida!")
main()

