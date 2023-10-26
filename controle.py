import json
estoque ={
    "gasolina": 1000,
    "alcool": 1500,
    "diesel": 1200
}

minLimite = {
    "gasolina": 300,
    "alcool": 250,
    "diesel": 200
}

def salvarEstoque(estoque):
    with open("estoque.json","w") as arquivo:
        json.dump(estoque,arquivo)

salvarEstoque(estoque)

def entrada(estoque,produto,quantidade):
    quantidade = int(quantidade)
    if produto in estoque:
        estoque[produto] += quantidade
        print(f"O produto {produto} entrou com {quantidade} litros.")
        salvarEstoque(estoque)
    else:
        print("Produto não encontrado.")

def saida(estoque,produto,quantidade):
    quantidade = int(quantidade)
    if produto in estoque and estoque[produto] >= quantidade:
        estoque[produto] -= quantidade
        print(f"{quantidade} L de {produto} foram vendidas.")
        salvarEstoque(estoque)
        alerta(produto,quantidade)
    else:
        alerta(produto,quantidade)
        print("Produto não encontrado ou estoque insuficiente.")

def carregarEstoque():
    try:
        with open("estoque.json","r") as arquivo:
            estoque_json = arquivo.read()
            estoque = json.loads(estoque_json)
        return estoque
    except FileNotFoundError:
        print("Arquivo não encontrado")
        return {}
def alerta(produto, quantidade):
    for produto,quantidade in estoque.items():
        if quantidade < minLimite[produto]:
            print("ALERTA!!")
            print(f"O estoque do produto {produto} esta abaixo do limite mínimo")


estoque = carregarEstoque()

while True:
    print("Controle de estoque da EcoEnergy")
    print("[1] vender combustivel")
    print("[2] comprar combustivel para o estoque")
    print("[3] sair")

    opcao = input("Insira a escolha ")

    if opcao == "1":
        produto = input("Insira o produto: [gasolina,alcool,diesel]")
        quantidade = input("Insira os litros do produto: ")
        saida(estoque,produto,quantidade)
    
    elif opcao == "2":
        prod = input("Insira o produto que quer comprar: [gasolina,alcool,diesel]")
        quant = input("Insira os litros do produto: ")
        entrada(estoque,prod,quant)

    elif opcao == "3":
        break