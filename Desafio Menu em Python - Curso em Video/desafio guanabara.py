#O desafio se trata de montar um sistema basico de cadastro de pessoas
#---------------------------------------------------------------------------------------------------------------------
#Função menu Principal
def ExibirMenu():
    print("-"*40)
    print("          MENU PRINCIPAL")
    print("-"*40)
    print("1 - Ver pessoas cadastradas")
    print("2 - Cadastrar nova pessoa")
    print("3 - Sair do Sistema")
#variaveis
resposta="sim"
pessoa=str
idade=0
#listas
PessoasCadastradas=[]
IdadePessoas=[]
while resposta != "3":
    ExibirMenu()
    resposta=str(input("Escolha a opção"))
    if resposta == "1":
        for n in range(len(PessoasCadastradas)):
            print("-----Pessoa {}-----".format(n+1))
            print("Nome",PessoasCadastradas[n])
            print("Idade",IdadePessoas[n])
    elif resposta == "2":
        pessoa=input("Digite o nome da pessoa")
        idade=int(input("Digite a idade da Pessoa"))
        PessoasCadastradas.append(pessoa)
        IdadePessoas.append(idade)
    elif resposta == "3":
        print("Fim do Programa")
        break
    else:
        print("Opção invalida, Escolha novamente")