import pandas as pd

class RelatorioNegocio:
    def __init__(self):
        self.arquivo_vendas = 'vendas.csv'
        self.arquivo_servicos = 'servicos.csv'
        self.df_vendas = self.carregar_dados(self.arquivo_vendas, ['Data', 'Vendas'])
        self.df_servicos = self.carregar_dados(self.arquivo_servicos, ['Tempo_Medio', 'Satisfacao_Cliente'])

    def carregar_dados(self, arquivo, colunas):
        try:
            return pd.read_csv(arquivo)
        except FileNotFoundError:
            return pd.DataFrame(columns=colunas)

    def salvar_dados(self, arquivo, dataframe):
        dataframe.to_csv(arquivo, index=False)

    def adicionar_venda(self, data, vendas):
        nova_venda = pd.DataFrame([[data, vendas]], columns=['Data', 'Vendas'])
        self.df_vendas = pd.concat([self.df_vendas, nova_venda], ignore_index=True)
        self.salvar_dados(self.arquivo_vendas, self.df_vendas)

    def adicionar_servico(self, tempo_medio, satisfacao_cliente):
        novo_servico = pd.DataFrame([[tempo_medio, satisfacao_cliente]], columns=['Tempo_Medio', 'Satisfacao_Cliente'])
        self.df_servicos = pd.concat([self.df_servicos, novo_servico], ignore_index=True)
        self.salvar_dados(self.arquivo_servicos, self.df_servicos)

    def gerar_relatorio_vendas(self):
        print("Relatório de Vendas:")
        print(self.df_vendas)

    def gerar_relatorio_servicos(self):
        print("Relatório de Serviços:")
        print(self.df_servicos)

# Exemplo de uso
relatorio_negocio = RelatorioNegocio()

# Entradas do usuário para vendas
data_venda = input("Informe a data da venda (YYYY-MM-DD): ")
vendas = float(input("Informe o valor das vendas: "))
relatorio_negocio.adicionar_venda(data_venda, vendas)

# Entradas do usuário para serviços
tempo_medio = float(input("Informe o tempo médio de execução do serviço (em horas): "))
satisfacao_cliente = float(input("Informe a satisfação do cliente (de 1 a 5): "))
relatorio_negocio.adicionar_servico(tempo_medio, satisfacao_cliente)

# Gerar relatórios
relatorio_negocio.gerar_relatorio_vendas()
relatorio_negocio.gerar_relatorio_servicos()
