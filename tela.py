# Imports 
import datetime
# Exceções personalizadas
class VerificaError(Exception):
     pass


#Funções

def hora(nome):
    hora= datetime.datetime.now()
    if (hora.hour >= 4 and hora.hour < 12):
        print(f"Bom dia {nome} !! \nComo posso ajudar hoje ? ")
    elif (hora.hour > 12 and hora.hour <=18):
         print(f"Bom tarde {nome} !! \nComo posso ajudar hoje ? ")
    else:
        print("Boa noite {nome} !! \nComo posso ajudar hoje ?")
 
def produtoscadastro():
    print("Funcionando")
    # Adicionar tudo que o usuuario cadastrar para a cupula

def produtos():
    print("Funcionando")
    #Fazer lista de produtos adicionados, e caso não tenha nada, exibir 



def opcoes():
    opcao = True
    print("1- Cadastro de produtos")
    print("2- Produtos")
    print("3- Encerrar cúpula \n")
    while (opcao):
        try:
            opcao = int(input("Digite uma opção: "))
            if (opcao <= 0 or opcao > 3):
                raise VerificaError
        except ValueError:
            print("ERRO: O valor informado não é um número \n")
        except VerificaError:
            print("ERRO: Digite apenas as opções exibidas \n")
        else:
            if (opcao == 1):
                produtoscadastro() 
                #Por enquanto deixar = false, mas depois chamar o incio do programa para ele escolher o produto cadastrado
                opcao = False
            elif (opcao == 2):
                produtos()
                # Deixar = false, pois quando ele escolher o produto, printa o necessario para ele e finaliza o programa 
                opcao = False
            elif (opcao == 3):
                print("Cúpula desligada !")
                opcao = False
        


def menu():
    print("BEM VINDO(A) A \n")#COLOCAR O NOME DA CUPULA

    nome = input("Digite seu nome: ")
    hora(nome)



opcoes()


