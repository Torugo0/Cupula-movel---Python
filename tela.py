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
         print(f"Boa tarde {nome} !! \nComo posso ajudar hoje ? \n")
    else:
        print("Boa noite {nome} !! \nComo posso ajudar hoje ? \n") 

def busca(cont, escolha):
    for item in cont:
        if item == escolha:
            return True
    return False

#Funções de produtos cadastro 

def cadastrar_cultivar():
    cultivar = input("Digite o nome da semente para cultivo: ")
    cultivar = cultivar.upper()
    nome_cultivar.append(cultivar)
    return cultivar

def cadastrar_temperatura(cultivar):
    while True:
        try:
            temperatura = float(input(f"Digite a temperatura ideal do(a) {cultivar}: "))
            temperatura_ideal.append(temperatura) 
            break
        except ValueError:
            print("ERRO: O valor informado não é um número ou contem valores errados (EX: 20)\n")

def cadastrar_luz():
    print("\n")
    while True:    
        try:
            print("Quantidade de luz: ")
            print("1- Baixa")
            print("2- Média")
            print("3- Alta \n")
            luz = int(input("Escolha uma das opções: "))
            if (luz < 1 or luz > 3):
                raise VerificaError
            print("\n")

            if (luz == 1):
                luz = "Baixa"
            elif (luz == 2):
                luz = "Média"
            elif (luz == 3):
                luz = "Alta"

            luz_ideal.append(luz)
            break
        except ValueError:
            print("ERRO: O valor informado não é um número \n")
        except VerificaError:
            print("ERRO: Digite apenas as opções exibidas \n")

def cadastrar_agua():
    while True:
        try:
            print("Quantidade de água: ")
            print("1- Pouca")
            print("2- Moderada")
            print("3- Alta \n")
            agua = int(input("Escolha uma das opções: "))
            if (agua < 1 or agua > 3):
                raise VerificaError
            print("\n")

            if (agua == 1):
                agua = "Pouca"
            elif (agua == 2):
                agua = "Moderada"
            elif (agua == 3):
                agua = "Alta"

            quantidade_agua.append(agua)
            break
        except ValueError:
            print("ERRO: O valor informado não é um número \n")
        except VerificaError:
            print("ERRO: Digite apenas as opções exibidas \n")

def cadastrar_tempo(cultivar):
    while True:
        try:
            print(f"Tempo de desenvolvivento do(a) {cultivar}")
            print("1- Dias")
            print("2- Meses")
            print("3- Anos \n")
            tempo = int(input("Escolha uma das opções: "))
            if (tempo < 1 or tempo > 3):
                raise VerificaError
            print("\n")

            if tempo == 1:
                while True:
                    try:
                        desenvolvimento = int(input("Quantos dia(s) serão necessários: "))
                        print("\n")
                        desenvolvimento = f"{desenvolvimento} dia(s)"
                        break
                    except ValueError:
                        print("ERRO: O valor informado não é um número \n")
            elif tempo == 2:
                while True:
                    try:
                        desenvolvimento = int(input("Quantos meses serão necessários: "))
                        if (desenvolvimento < 0 or desenvolvimento > 12):
                            raise VerificaError
                        print("\n")
                        desenvolvimento = f"{desenvolvimento} mês(es)"
                        break
                    except ValueError:
                        print("ERRO: O valor informado não é um número \n")
                    except VerificaError:
                        print("ERRO: Digite os meses entre 1 e 12 \n")
            elif tempo == 3:
                while True:
                    try:
                        desenvolvimento = int(input("Quantos ano(s) serão necessários: "))
                        print("\n")
                        desenvolvimento = f"{desenvolvimento} ano(s)"
                        break
                    except ValueError:
                        print("ERRO: O valor informado não é um número \n")

            tempo_desenvolvimento.append(desenvolvimento)
            break
        except ValueError:
            print("ERRO: O valor informado não é um número \n")
        except VerificaError:
            print("ERRO: Digite apenas as opções exibidas \n")

def produtoscadastro():
    print("\n")
    cultivar = cadastrar_cultivar()
    cadastrar_temperatura(cultivar)
    cadastrar_luz()
    cadastrar_agua()
    cadastrar_tempo(cultivar)
    
    print("O produto foi cadastrado com sucesso ! \nAcesse-o(a) na opção (2- Produtos) e ative a cúpula \n")
    opcoes()

    # Adicionar tudo que o usuario cadastrar para a cupula 

#Funções de produtos

def escolha_final(cont, escolha, roda):
    roda = True
    while (roda):
        if busca(cont,escolha):
            print(f"Ligar capsula para: {nome_cultivar[escolha-1]} ?")
            final = input("Sim ou Não: ")
            print("\n")
            final = final.upper()

            if (final == "SIM"):
                print("Ativando cúpula")
                break
            elif(final == "NÃO" or final == "NAO"):
                print("Voltando ao menu principal \n")
                opcoes()
                break
            else:
                raise VerificaError

def produtos():
    if (len(nome_cultivar) == 0):
        print("Não há produtos cadastrados, adicione-os em (1- Cadastro de produtos) \n")
        opcoes()
    else:
        roda = True
        while roda:
            try:
                soma = 1
                cont = [1]
                for i in range(len(nome_cultivar)):
                    print(f"{cont[i]}- {nome_cultivar[i]} \n - Temperatura: {temperatura_ideal[i]}\n - Luz: {luz_ideal[i]}\n - Água: {quantidade_agua[i]}\n - Tempo: {tempo_desenvolvimento[i]}")
                    soma += 1
                    cont.append(soma)
                    print("\n")
            
                escolha = int(input("Escolha um produto para ativar a capsula (Digite 0 para voltar ao menu principal): "))
                print("\n")
                if (escolha == 0):
                    opcoes()
                    break

                escolha_final(cont, escolha, roda)
                break
            except IndexError:
                print("ERRO: Escolha os produtos exibidos em tela ou os adicione em (1- Cadastro de produtos)\n")
            except ValueError:
                print("Digite apenas números \n")
            except VerificaError:
                print("Digite apenas Sim ou Não \n")
                escolha_final(cont, escolha, roda)
                break

# Funções para exclusão do produto

def produtosexcluir(escolha):
    nome_cultivar.pop(escolha-1)
    temperatura_ideal.pop(escolha-1)
    luz_ideal.pop(escolha-1)
    quantidade_agua.pop(escolha-1)
    tempo_desenvolvimento.pop(escolha-1)



def excluir_final(cont, escolha, roda):
    roda = True
    while (roda):
        if busca(cont,escolha):
            print(f"Excluir: {nome_cultivar[escolha-1]} ?")
            final = input("Sim ou Não: ")
            print("\n")
            final = final.upper()

            if (final == "SIM"):
                print(f"{nome_cultivar[escolha-1]} foi removido com sucesso ! \nVoltando ao menu principal \n")
                produtosexcluir(escolha)
                opcoes()
                break
            elif(final == "NÃO" or final == "NAO"):
                print("Voltando ao menu principal \n")
                opcoes()
                break
            else:
                raise VerificaError


def excluirproduto():
    if (len(nome_cultivar) == 0):
        print("Não há produtos cadastrados para excluir, adicione-os em (1- Cadastro de produtos) \n")
        opcoes()
    else:
        roda = True
        while roda:
            try:
                soma = 1
                cont = [1]
                for i in range(len(nome_cultivar)):
                    print(f"{cont[i]}- {nome_cultivar[i]} \n - Temperatura: {temperatura_ideal[i]}\n - Luz: {luz_ideal[i]}\n - Água: {quantidade_agua[i]}\n - Tempo: {tempo_desenvolvimento[i]}")
                    soma += 1
                    cont.append(soma)
                    print("\n")
            
                escolha = int(input("Escolha um produto para excluir do histórico da cúpula (Digite 0 para voltar ao menu principal): "))
                print("\n")
                if (escolha == 0):
                    opcoes()
                    break

                excluir_final(cont, escolha, roda)
                break
            except IndexError:
                print("ERRO: Escolha os produtos exibidos em tela ou os adicione em (1- Cadastro de produtos)\n")
            except ValueError:
                print("Digite apenas números \n")
            except VerificaError:
                print("Digite apenas Sim ou Não \n")
                excluir_final(cont, escolha, roda)
                break



#Funções opções
def menu_opçoes():
    print("MENU PRINCIPAL")
    print(" 1- Cadastro de produtos")
    print(" 2- Produtos")
    print(" 3- Excluir produto")
    print(" 4- Encerrar cúpula \n")
    while True:
        try:
            opcao = int(input("Digite uma opção: "))
            print("\n")
            if (opcao < 1 or opcao > 4):
                raise VerificaError
            return opcao
        except ValueError:
            print("ERRO: O valor informado não é um número \n")
        except VerificaError:
            print("ERRO: Digite apenas as opções exibidas \n")

def opcoes():
    opcao = menu_opçoes()
    match opcao:
        case 1:
            produtoscadastro()
        case 2:
            produtos()
        case 3:
            excluirproduto()
        case 4:
            print("Cúpula desligada !")


# Parte principal
def menu():
    print("BEM VINDO(A) A CÚPULA EATABLE GARDEN\n")
    hora()
    opcoes()


menu()