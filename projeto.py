def linhas(nome):
    print(f"="*40)
    print(nome)
    print("="*40)

def imprimir_dados(arquivo):
    with open(arquivo, 'r') as arquivo:
        for linha in arquivo:
            linha_sem = linha.replace(",", ":").replace("(", "").replace(")", "").replace("'", "")
            print(linha_sem, end='')

opcao = ""

funcionarios = [ "Adenair", "Jorge", "Alberto", "Helena", "Benjamin", "Ayla", "Bentancur" ]
servicos = ["Oleo", "Balanceamento"]
registro = {}
veiculos = {"xyz-3344": "29.12",
            "abc-1234": "30.10",
            "php-3456": "21.09"}
funcionarios = {
            "Adenair":  "Disponivel",
            "Jorge" : "Disponivel",
            "Alberto" :  "Disponivel",
            "Helena" :  "Disponivel",
            "Benjamin" :  "Disponivel",
            "Ayla" : "Disponivel",
            "Bentancur" : "Disponivel"
        }
print("Bem vindo a area de gerenciamento de serviços automotivos, para prosseguir basta escolher uma das opções abaixo!\n")

while True: 
    print("\n[0] Imprima a tabela dos registros anteriores")
    print("[1] Fazer um novo registro")
    print("[2] Adicionar um novo veiculo no histórico")
    print("[3] Ver Histórico de veiculos")
    print("[4] Agendamento de Serviço")
    print("[5] sair\n")
    
    while True:
        try:
            escolha_inicial = int(input("Escolha sua opção: "))
            break
        except ValueError:
            print("Opção inválida")
    match escolha_inicial:
#imprimi os registros anteriores
        case 0:
            if registro == "":
                print("A lista de registro está vazia")
            with open ("Registros.txt", "r")as arquivo:
                for linha in arquivo:
                    print(linha)
                print("\n")
#faz um novo registro
        case 1:
            opcao_hora = ""
            opcao_funcionarios = ""
            opcao = ""
            opcao_servicos= ""
            while opcao != "N" :
                linhas("Funcionários")
                for nomes in funcionarios:
                    print(nomes)
                print("\n")

                opcao_funcionarios = input("Funcionário que realizou o serviço: ")
                opcao_funcionarios = opcao_funcionarios.capitalize()
                if opcao_funcionarios in funcionarios:
                    
                    linhas("Serviços")
                    for tarefas in servicos:
                        print(tarefas)
                    print("\n")

                    opcao_servicos = input("Serviço realizado: ")
                    opcao_servicos = opcao_servicos.capitalize()
                    if opcao_servicos in servicos:
                        while True:
                            try:
                                opcao_hora = int(input("Tempo do serviço em minutos: "))
                                opcao_pecas = int(input("Quantidade de peças utilizadas: "))
                                break
                            except ValueError:
                                print("opção inválida, tente novamente")

                        if opcao_servicos in servicos:
                            registro[opcao_funcionarios] = opcao_servicos
                            print("Registro salvo com sucesso!")
                            with open("Registros.txt", "a") as arquivo:
                                arquivo.write(f"{nomes} - {servicos} - {opcao_hora} - {opcao_pecas}")

#escolha de sim ou não para registro
                            while True:
                                opcao = input("Deseja marcar outra consulta? [s/n]: ")
                                opcao = opcao.capitalize()
                                if opcao != "S" and opcao != "N":
                                     print("Opção inválida, por favor insira S(sim) ou N(não)")
                                elif opcao == "S":
                                    break
                                elif opcao == "N":
                                    print("\nRegistro encerrado")
                                    break
                    else:
                        print("Serviço inválido, por favor tente novamente!\n")

                else:
                    print("Funcionário não encontrado, por favor tente novamente!\n")

        
#adicionar um novo veiculo ao historico 
        case 2:
            escolha_historico = ""
            while escolha_historico != "N":
                
                print("\ninforme a placa do veiculo\n")
                placa_letra = input("Digite as letras(3 digitos): ")

                if len(placa_letra) == 3:
                    placa_numero = input("Digite o número(4 digitos): ") 
                    if len(placa_numero) == 4:
                        while True:
                            try:
                                dia = int(input("Informe o dia: "))
                                mes = int(input("informe o mês: "))
                                if mes <=12 and dia <=31:
                                    break
                                else:
                                    print("Data inválida, tente novamente")
                            except ValueError:
                                print("Data inválida, tente novamente")
                        
                        veiculos[f"{placa_letra}-{placa_numero}"] = f"{dia}.{mes}"
                        print("Veiculo adicionado com sucesso!!")
                        with open ("historico.txt", "w") as arquivo:
                            arquivo.write("placa - data - funcionario - serviço\n")
                            for letra, numero in veiculos.items():
                                arquivo.write(f"\n{letra} : {numero} - {opcao_funcionarios} - {opcao_servicos}")
#escolha de sim ou não para o historico
                        while True:
                                escolha_historico = input("Deseja adicionar outro veículo? [s/n]: ")
                                escolha_historico = escolha_historico.capitalize()
                                if escolha_historico != "S" and escolha_historico != "N":
                                     print("Opção inválida, por favor insira S(sim) ou N(não)")
                                elif escolha_historico == "S":
                                    break
                                elif escolha_historico == "N":
                                    print("\nHistórico encerrado")
                                    break


                        
                        
                    else:
                        print("Número(s) inválido(s), por favor tente novamente")            
                else:
                    print("Letra(s) inválida(s), por favor tente novamente")
#imprimi o historico dos veiculos
        case 3:
            linhas("histórico dos veiculos")
            with open ("historico.txt", "r") as arquivo:
                for linha in arquivo:
                    print(linha)
#agendamento dos serviços
        case 4:
            print("Bem-vindo à nossa plataforma de agendamento de serviços,\nonde facilitamos o processo para você agendar seu atendimento\nem nosso estabelecimento!\n")
            
            opcao = ""
            while opcao != "N":
                
                imprimir_dados("funcionarios.txt")


                escolha = input("\nEscolha um funcionário: ")
                maiusculo = escolha.capitalize()
                if  maiusculo in funcionarios:
                    if funcionarios[maiusculo] == "Disponivel":
                        while True:   
                            try:
                                escolha_hora = int(input("Escolha a hora do agendamento: "))
                                escolha_minuto = int(input("Escolha os minutos do agendamento: "))
                                break
                            except ValueError:    
                                print("opção Inválida, tente novamente")
                        
                        if escolha_hora <= 22 and escolha_minuto <= 60:
                            
                            if maiusculo in funcionarios.keys():
                                funcionarios[maiusculo] = f"Horario marcado as {escolha_hora}:{escolha_minuto}"
                                
                                print("\nHorário reservado com sucesso!!")
#escolha de sim ou não para o agendamento                           
                                while True:
                                    opcao = input("Deseja marcar outra consulta? [s/n]: ")
                                    opcao = opcao.capitalize()
                                    if opcao != "S" and opcao != "N":
                                        print("Opção inválida, por favor insira S(sim) ou N(não)")
                                    elif opcao == "s":
                                        with open ("funcionarios.txt", "w") as arquivo:
                                            for valor in funcionarios.items():
                                                arquivo.write(str(valor) + '\n')
                                        break
                                    elif opcao == "N":
                                        print("Função encerrada")
                                        
                                        with open ("funcionarios.txt", "w") as arquivo:
                                            for valor in funcionarios.items():
                                                arquivo.write(str(valor) + '\n')

                                        break        
                    
                    

                        else:
                            print("Horário invalido!\n")            
                    else:
                        print("O funcionário escolhido já possui horário marcado, tente novamente!\n")
                else:
                        print("Funcionário não encontrado, por favor tente novamente")        

 
#encerra o programa 
        case 5:
            print("\nPrograma encerrado, obrigado pela preferência!!")
            break 
                        
        case _:
            print("Opção inválida")

        