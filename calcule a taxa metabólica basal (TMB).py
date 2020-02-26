###Função Para calcular a taxa metabólica basal (TMB).
def parametro (kg,gp):
    codigo=[1,2,3,4,5]
    constante=[129,78,70,49,10]
    nome=["passeriformes","não passeriformes","mamiferos placentarios","masurpiais e endetatas","répteis"]
    c=gp
    k=constante[c-1]
    tmb=(kg**0.75)*k
    return tmb
def main():

    kg=int(input("digite o kg do animal"))
    nome = [" 1 passeriformes", "2 não passeriformes", "3 mamiferos placentarios", "4 masurpiais e endetatas", "5 répteis"]
    print(nome)
    gp=int(input("digite o codigo do grupo do animal  "))
    print("o PMV é {:.2f}".format(parametro(kg,gp)))
main()
