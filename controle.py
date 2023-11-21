import csv
import pandas as pd
estoque_inicial ={
    "gasolina": 1000,
    "alcool": 1500,
    "diesel": 1200
}
minLimite = {
    "gasolina": 300,
    "alcool": 250,
    "diesel": 200
}
# a complexidade total da função entrada é O(n) 
# Se a condição for verdadeira, há uma operação de incremento (estoque_gasolina[produto] += quantidade), que também é uma operação de tempo constante O(1).
def entrada(produto,quantidade):
    for item in estoque_inicial:
        if item == produto:
            estoque_inicial[produto] += quantidade
   
# a complexidade total da função saída é O(n)
# Se a condição for verdadeira, há uma operação de decremento (estoque_gasolina[produto] -= quantidade), que também é uma operação de tempo constante O(1).
def saida(produto,quantidade):
    for item in estoque_inicial:
        if item == produto:
            estoque_inicial[produto] -= quantidade
    
# a complexidade total da função alerta é O(n) onde n é o número de produtos no estoque  
def alerta(produto, quantidade):
    for produto,quantidade in estoque_inicial.items():
        if quantidade < minLimite[produto]:
            print("ALERTA!!")
            print(f"O estoque do produto {produto} esta abaixo do limite mínimo")



while True:
    print("Controle de estoque da EcoEnergy")
    print("[1] vender combustivel")
    print("[2] comprar combustivel para o estoque")
    print("[3] sair")

    opcao = input("Insira a escolha ")
    print(estoque_inicial)

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
inserir = pd.DataFrame.from_dict(estoque_inicial, orient='index',columns=['estoque'])
inserir.to_csv('estoque.csv', mode='a')
inserir = inserir.sort_values(by='estoque')
inserir.to_csv('estoque.csv')
inserir = pd.read_csv('estoque.csv',index_col=0)
inserir.head()