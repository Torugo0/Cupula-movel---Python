# Imports 
import datetime

# Exceções personalizadas
class VerificaError(Exception):
     pass

# Variaveis
nome_cultivar = []
temperatura_ideal = []
luz_ideal = []
quantidade_agua = []
tempo_desenvolvimento = []

#Funções

def hora():
    nome = input("Digite seu nome: ")
    hora= datetime.datetime.now()
    if (hora.hour >= 4 and hora.hour < 12):
        print(f"Bom dia {nome} !! \nComo posso ajudar hoje ? \n")
    elif (hora.hour > 12 and hora.hour <=18):
         print(f"Bom tarde {nome} !! \nComo posso ajudar hoje ? \n")
    else:
        print("Boa noite {nome} !! \nComo posso ajudar hoje ? \n") 

#Funções de produtos cadastro 





def produtoscadastro():
    roda = True
    while (roda):
        cultivar = input("Digite o nome da semente para cultivo: ")
        nome_cultivar.append(cultivar)

        temperatura = float(input(f"Digite a temperatura ideal do(a) {cultivar}: "))
        temperatura_ideal.append(temperatura) 
        print("\n")

        print("Quantidade de luz: ")
        print("1- Baixa")
        print("2- Média")
        print("3- Alta")
        luz = int(input("Escolha uma das opções: \n"))
        print("\n")
        if (luz == 1):
            luz = "Baixa"
            luz_ideal.append(luz)
        elif (luz == 2):
            luz = "Média"
            luz_ideal.append(luz)
        elif (luz == 3):
            luz = "Alta"
            luz_ideal.append(luz)
        
        print("Quantidade de água: ")
        print("1- Pouca")
        print("2- Moderada")
        print("3- Alta")
        agua = int(input("Escolha uma das opções: \n"))
        print("\n")
        if (agua == 1):
            agua = "Pouca"
            quantidade_agua.append(agua)
        elif (agua == 2):
            agua = "Moderada"
            quantidade_agua.append(agua)
        elif (agua == 3):
            agua = "Alta"
            quantidade_agua.append(agua)
        
        print(f"Tempo de desenvolvivento do(a) {cultivar}")
        print("1- Dias")
        print("2- Meses")
        print("3- Anos \n")
        tempo = int(input("Escolha uma das opções: "))
        print("\n")
        if (tempo == 1):
            desenvolvimento = int(input("Quantos dia(s) serão necessários: \n"))
            desenvolvimento = (f"{desenvolvimento} dia(s)")
            tempo_desenvolvimento.append(desenvolvimento)
        elif (tempo == 2):
            desenvolvimento = int(input("Quantos meses serão necessários: \n"))
            desenvolvimento = (f"{desenvolvimento} mês(es)")
            tempo_desenvolvimento.append(desenvolvimento)
        elif (tempo == 3):
            desenvolvimento = int(input("Quantos ano(s) serão necessários: \n"))
            desenvolvimento = (f"{desenvolvimento} ano(s)")
        print("O produto foi cadastrado com sucesso ! \nAcesse-o(a) na opção (2- Produtos) e ative a cúpula \n")
        roda = False
    opcoes()

    # Adicionar tudo que o usuario cadastrar para a cupula 

#Funções de produtos

def produtos():
    print("Funcionando")
    #Fazer lista de produtos adicionados, e caso não tenha nada, exibir 



#Funções opções
def menu_opçoes():
    print("1- Cadastro de produtos")
    print("2- Produtos")
    print("3- Encerrar cúpula \n")
    while True:
        try:
            opcao = int(input("Digite uma opção: "))
            print("\n")
            if (opcao < 1 or opcao > 3):
                raise VerificaError
            return opcao
        except ValueError:
            print("ERRO: O valor informado não é um número \n")
        except VerificaError:
            print("ERRO: Digite apenas as opções exibidas \n")

def opcoes():
    opcao = menu_opçoes() # Feito
    match opcao:
        case 1:
            produtoscadastro() #Separar em def's e fazer tratamento de erros
        case 2:
            produtos()
        case 3:
            print("Cúpula desligada !")
#Dentro de cada uma delas colocar o false para não entrar em loop infinito



# Parte principal
def menu():
    print("BEM VINDO(A) A \n")#COLOCAR O NOME DA CUPULA

    hora()

    opcoes()

menu()