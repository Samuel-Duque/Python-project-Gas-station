import csv
import random
import pandas as pd
estoque_gasolina ={
    "gasolina": 1000,
    "alcool": 1500,
    "diesel": 1200
}
minLimite = {
    "gasolina": 300,
    "alcool": 250,
    "diesel": 200
}
#criar o arquivo csv
# with open('estoque.csv', "w", newline='') as arquivo:
#     cabecalho = ['produto', 'estoque']
#     escritor_csv = csv.DictWriter(arquivo, fieldnames=cabecalho)
#     escritor_csv.writeheader()


        
def salvarEstoque(dados):
    with open('estoque.csv', "w", newline='') as arquivo:
        cabecalho = ['produto', 'estoque']
        escritor_csv = csv.DictWriter(arquivo, fieldnames=cabecalho)
        escritor_csv.writeheader()
        escritor_csv.writerows(dados)

def obterEstoque():
    try:
        with open('estoque.csv', "r") as arquivo:
            leitor_csv = csv.DictReader(arquivo)
            dados = list(leitor_csv)
        return dados
    except FileNotFoundError:
        return []

def entrada(produto,quantidade):
    for item in estoque_gasolina:
        if item == produto:
            estoque_gasolina[produto] += quantidade
    # estoquee = obterEstoque()
    # quantidade = int(quantidade)
    # produto_encontrado = False
    # for item in estoquee:
    #     if item['produto'] == produto:
    #         item['estoque'] = int(item['estoque']) + quantidade
    #         produto_encontrado = True
    #     estoque_ordenado = ordenarEstoquePorQuantidade(estoquee)
    #     salvarEstoque(estoque_ordenado)
    
def ordenarEstoquePorQuantidade(estoque):
    return sorted(estoque, key=lambda x: int(x['estoque']))

def saida(produto,quantidade):
    for item in estoque_gasolina:
        if item == produto:
            estoque_gasolina[produto] -= quantidade
        # estoques = obterEstoque()
    # quantidade = int(quantidade)
    # for item in estoques:
    #     if item['produto'] == produto:
    #         quantidade_atual = int(item['estoque'])
    #         if quantidade_atual >= quantidade:
    #             item['estoque'] = quantidade_atual - quantidade
    #         else:
    #             print("Quantidade insuficiente em estoque.")
    #             return
    # estoque_ordenado = ordenarEstoquePorQuantidade(estoques)
    # salvarEstoque(estoque_ordenado)

def carregarEstoque():
    
    try:
        with open("estoque.csv","r") as arquivo:
            estoque = arquivo.read()
            estoque = csv.DictReader(arquivo)
        return estoque
    except FileNotFoundError:
        print("Arquivo não encontrado")
        return {}
    
def alerta(produto, quantidade):
    for produto,quantidade in estoque.items():
        if quantidade < minLimite[produto]:
            print("ALERTA!!")
            print(f"O estoque do produto {produto} esta abaixo do limite mínimo")



while True:
    print("Controle de estoque da EcoEnergy")
    print("[1] vender combustivel")
    print("[2] comprar combustivel para o estoque")
    print("[3] sair")

    opcao = input("Insira a escolha ")
    print(estoque_gasolina)

    if opcao == "1":
        produto = input("Insira o produto: [gasolina,alcool,diesel]")
        quantidade = int(input("Insira os litros do produto: "))
        saida(produto,quantidade)

    elif opcao == "2":
        prod = input("Insira o produto que quer comprar: [gasolina,alcool,diesel]")
        quant = int(input("Insira os litros do produto: "))
        entrada(prod,quant)

    elif opcao == "3":
        break
    #fazer o arquivo
inserir = pd.DataFrame.from_dict(estoque_gasolina, orient='index',columns=['estoque'])
inserir.to_csv('estoque.csv', mode='a')
inserir = inserir.sort_values(by='estoque')
inserir.to_csv('estoque.csv')
inserir = pd.read_csv('estoque.csv',index_col=0)
inserir.head()