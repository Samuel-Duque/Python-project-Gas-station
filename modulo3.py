# Autor: José Vinicius - Módulo 3 - 29/10/23

class Produto:
    def __init__(self, produto, quantidade, peso, valor, qtdInicial, repor, qtdVendida):
        self.nomeProduto = produto
        self.quantidade = quantidade
        self.valor = valor
        self.peso = peso
        self.qtdInicial = qtdInicial
        self.repor = repor
        self.qtdVendida = qtdVendida

#Produtos Iniciais
produto1 = Produto("Alface", 50, 0.5, 2, 10, False, 0)
produto2 = Produto("Maca", 30, 0.3, 1, 6, False,0)


produtos = [
    produto1,
    produto2
]
valorTotalVendas = 0


def menuInicial(valorTotalVendas):
    print("\n---- Bem vindo a Mercearia ----\n\n1. Vender produtos\n2. Adicionar Produto a Mercearia\n3. Remover Produto da Mercearia\n4. Visualizar estoque de produtos\n5. Análise de desempenho\n")
    escolhaMenu = int(input("\nDigite o numero da opcao desejada: "))

    match escolhaMenu:
        case 1:
            vender(valorTotalVendas)
        case 2:
            adicionarProduto()
        case 3:
            removerProduto()
        case 4:
            inFucao = False
            visualizarEstoque(inFucao)
        case 5:
            analiseDesempenho(valorTotalVendas)
        case _:
            print("\nOpção inválida, tente novamente!\n")
            menuInicial(valorTotalVendas)  

def vender(valorTotalVendas):
    count = -1
    inFuncao = True
    visualizarEstoque(inFuncao)

    print("\n - Vender Produto - ")
    escolhaProd = input("Escolha o produto que deseja vender: ")
    for produto in produtos:
        count += 1
        if count == len(produtos):
            print("\nProduto não encontrado, tente novamente!")
            vender(valorTotalVendas)
        if escolhaProd == produto.nomeProduto:
            print(f"\nProduto {produto.nomeProduto} encontrado!")
            escolhaQuantidade = int(input("Digite a quantidade que deseja vender: "))
            if escolhaQuantidade > int(produto.quantidade):
                print("\nQuantidade indisponível!")
                with open("relatorioAlertas.txt" , "a") as arquivo:
                    arquivo.write(f"| QTD INDISPONIVEL | Produto: {produto.nomeProduto} | Quantidade: {produto.quantidade} |\n")
                vender(valorTotalVendas)
            else:
                produto.quantidade -= escolhaQuantidade
                if produto.quantidade <= produto.qtdInicial:
                    produto.repor = True
                valorTotalVendas += produto.valor * escolhaQuantidade    
                with open("relatorioVendas.txt" , "a") as arquivo:
                    arquivo.write(f"Produto: {produto.nomeProduto} | Quantidade: {escolhaQuantidade} | Valor Total: R${produto.valor * escolhaQuantidade}\n")
                print(f"\nVenda realizada com sucesso! Valor total: R${produto.valor * escolhaQuantidade}")
                produto.qtdVendida +=1
                if produto.repor == True:
                    print(f"\n- ATENÇÃO -  O produto {produto.nomeProduto} precisa ser reposto!\n")
                    with open("relatorioAlertas.txt" , "a") as arquivo:
                        arquivo.write(f"| REPOSICAO | Produto: {produto.nomeProduto} | Quantidade: {produto.quantidade} |\n")    
                menuInicial(valorTotalVendas)

def adicionarProduto():
    print("\n - Adicionar Produto - ")

    NomeProduto = input("Digite o nome do produto: ")
    QuantidadeProduto = int(input("Digite a quantidade do produto: "))
    PesoProduto = input("Digite o peso do produto em Kg: ")
    ValorProduto = float(input("Digite o valor unitario do produto em Reais (R$): "))
    qtdInicial = ((QuantidadeProduto * 20) / 100)
    novoProduto = Produto(NomeProduto, QuantidadeProduto, PesoProduto, ValorProduto, qtdInicial, False, 0)
    produtos.append(novoProduto)
        
    menuInicial(valorTotalVendas)

def removerProduto():
    inFuncao = True
    visualizarEstoque(inFuncao)
    print("\n - Remover Produto - ")
    escolhaProd = input("Escolha o produto que deseja remover: ")
    count = 0
    for produto in produtos:   
        count += 1    
        if count == len(produtos):
            print("\nProduto não encontrado, tente novamente!")
            removerProduto()
        elif escolhaProd == produto.nomeProduto:
            produtos.remove(produto)
            print("Produto removido com sucesso!")
            menuInicial(valorTotalVendas)
def visualizarEstoque(inFuncao):
    count = 1
    print("\n\t- Estoque - ")
    for produto in produtos:
        print(f"Produto {count}: {produto.nomeProduto} | Quantidade: {produto.quantidade} | Valor: R${produto.valor} | Peso: {produto.peso}Kg | Repor: {produto.repor}")
        count += 1
    if inFuncao == False:
        input("\nPressione qualquer tecla para voltar ao menu inicial")    
        menuInicial(valorTotalVendas)

def analiseDesempenho(valorTotalVendas):
    maisVendido = None
    aux = 0
    count = 0
    print("\n - Análise de Desempenho - ")
    print(f"Total em Vendas: R${valorTotalVendas}")
    for produto in produtos:
        count += 1
        if maisVendido == None:
            aux = produto.qtdVendida
            maisVendido = produto.nomeProduto
        elif produto.qtdVendida > aux:
            maisVendido = produto.nomeProduto
        if count == len(produtos):
            print(f"Produto mais vendido: {maisVendido}")
            
    menuInicial(valorTotalVendas)

def gerarAlertaQuantidade():
    pass

with open("relatorioVendas.txt" , "a") as arquivo:
    arquivo.write("\n - Relatorio de Vendas -\n")
with open("relatorioAlertas.txt" , "a") as arquivo:
    arquivo.write("\n - Relatorio de Alertas - \n")    
menuInicial(valorTotalVendas)
