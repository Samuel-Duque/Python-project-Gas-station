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
veiculos = {}
lista = []
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
    print("[1] Fazer registro e inserir no histórico")
    print("[2] imprimi o histórico dos veiculos")
    print("[3] Agendamento de Serviço")
    print("[4] sair\n")
    
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
            with open ("Registros.txt", "r") as arquivo:
                for linha in arquivo:
                    print(linha)
                print("\n")
#faz um novo registro
        case 1:
            opcao = ""
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
                                arquivo.write(f"{opcao_funcionarios} - {opcao_servicos} - {opcao_hora} - {opcao_pecas}\n")



                            escolha_historico = ""
                    
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
                                    data = dia,"/", mes   
                                    veiculos[f"{placa_letra}-{placa_numero}"] = {"funcionario": opcao_funcionarios,
                                                                                "data": data,
                                                                                "serviços": opcao_servicos,
                                                                                "peças": opcao_pecas,
                                                                                "tempo de serviço": opcao_hora}
                                    print("Veiculo adicionado com sucesso!!")
                                    informacoes = veiculos[f"{placa_letra}-{placa_numero}"]
                                    with open ("historico.txt", "a") as arquivo:
               
                #escolha de sim ou não para o historico
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
        

#imprimi o historico dos veiculos
        case 2:
            linhas("histórico dos veiculos")
            with open ("historico.txt", "r") as arquivo:
                for linha in arquivo:
                    print(linha)
#agendamento dos serviços
        case 3:
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
                                    elif opcao == "S":
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
        case 4:
            print("\nPrograma encerrado, obrigado pela preferência!!")
            break 

        case 5:
            print(veiculos)                
        case _:
            print("Opção inválida")

        