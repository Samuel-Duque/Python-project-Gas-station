import csv



print("Bem-vindo à nossa plataforma de agendamento de serviços,\nonde facilitamos o processo para você agendar seu atendimento\nem nosso estabelecimento!\n")
funcionarios = {
    "Adenair":  "Disponivel",
    "Jorge" : "Disponivel",
    "Alberto" :  "Disponivel",
    "Helena" :  "Disponivel",
    "Benjamin" :  "Disponivel",
    "Ayla" : "Disponivel",
    "Bentancur" : "Disponivel"
}


opcao = ""
while opcao != "n":
    for nome, horario in funcionarios.items():
        print(nome,":", horario)


    escolha = input("\nEscolha um funcionário: ")
    if funcionarios[escolha] == "Disponivel":
        escolha_hora = int(input("Escolha a hora do agendamento: "))
        escolha_minuto = int(input("Escolha os minutos do agendamento: "))
        if escolha_hora <= 22 and escolha_minuto <= 60:
            if escolha in funcionarios.keys():
                funcionarios[escolha] = f"Horario marcado as {escolha_hora}:{escolha_minuto}"
                
                print("\nHorário reservado com sucesso!!")
                opcao = input("Deseja marcar outra consulta? [s/n]: ")
                print("\n")
                    
                while True:
                    if opcao != "s" and opcao != "n":
                        print("Digite novamente")
                    elif opcao == "s":
                        break
                    elif opcao == "n":
                        break
                       
        else:
            print("Horário invalido!\n")            
    else:
        print("O funcionário escolhido já possui horário marcado, tente novamente!\n")
    with open ("Funcionarios.csv", "w") as arquivo:
        arquivo.write(funcionarios)
