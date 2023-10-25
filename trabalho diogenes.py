import random as rd

geracao_mensal = 0

meses = {"jan":1,"fev":2,"mar":3,
         "abr":4,"mai":5,"jun":6,
         "jul":7,"ago":8,"set":9,
         "out":10,"nov":11,"dez":12}
alertas_log = {}

eventos_ponderados = [
    (1, 0.7),  # Coeficiente 1 com 70% de chance
    (0.8, 0.1),  # Coeficiente 0.8 com 10% de chance
    (0.2, 0.1),  # Coeficiente 0.2 com 10% de chance
    (0.4, 0.05),  # Coeficiente 0.4 com 5% de chance
    (0.0, 0.05),  # Coeficiente 0.0/ com 5% de chance
]

geracao_anual = []
total_alertas = 0

for mes_nome, mes_numero in meses.items():
    if mes_numero in [12, 1, 2]:
        for dia in range(1, 30):

            eventos_aleatorios = rd.choices(eventos_ponderados)
            for evento in eventos_aleatorios:
                aleatoriedade = evento[0]

            if aleatoriedade == 0:
                total_alertas += 1

                if mes_nome not in alertas_log:
                    alertas_log[mes_nome] = 1
                else:
                    alertas_log[mes_nome] += 1


            eficiencia = rd.uniform(0.9, 0.95)
            geracao_base_dia = 1000 * eficiencia * aleatoriedade
            geracao_mensal += geracao_base_dia

        
        print(f"Geração em {mes_nome}: {geracao_mensal:.0f} kWh")
        geracao_anual.append(geracao_mensal)
        geracao_mensal = 0          # Reinicie a geração mensal para o próximo mês.

    elif mes_numero in [3, 4, 5]:
        for dia in range(1, 30):

            eventos_aleatorios = rd.choices(eventos_ponderados)
            for evento in eventos_aleatorios:
                aleatoriedade = evento[0]

            if aleatoriedade == 0:
                total_alertas += 1

                if mes_nome not in alertas_log:
                    alertas_log[mes_nome] = 1
                else:
                    alertas_log[mes_nome] += 1


            eficiencia = rd.uniform(0.75, 0.85)
            geracao_base_dia = 1000 * eficiencia * aleatoriedade
            geracao_mensal += geracao_base_dia

        
        print(f"Geração em {mes_nome}: {geracao_mensal:.0f} kWh")
        geracao_anual.append(geracao_mensal)
        geracao_mensal = 0

    elif mes_numero in [6, 7, 8]:
        for dia in range(1, 30):

            eventos_aleatorios = rd.choices(eventos_ponderados)
            for evento in eventos_aleatorios:
                aleatoriedade = evento[0]

            if aleatoriedade == 0:
                total_alertas += 1

                if mes_nome not in alertas_log:
                    alertas_log[mes_nome] = 1
                else:
                    alertas_log[mes_nome] += 1


            eficiencia = rd.uniform(0.6, 0.7)
            geracao_base_dia = 1000 * eficiencia * aleatoriedade
            geracao_mensal += geracao_base_dia

        
        print(f"Geração em {mes_nome}: {geracao_mensal:.0f} kWh")
        geracao_anual.append(geracao_mensal)
        geracao_mensal = 0

    elif mes_numero in [9, 10, 11]:
        for dia in range(1, 30):

            eventos_aleatorios = rd.choices(eventos_ponderados)
            for evento in eventos_aleatorios:
                aleatoriedade = evento[0]

            if aleatoriedade == 0:
                total_alertas += 1

                if mes_nome not in alertas_log:
                    alertas_log[mes_nome] = 1
                else:
                    alertas_log[mes_nome] += 1


            eficiencia = rd.uniform(0.75, 0.85)
            geracao_base_dia = 1000 * eficiencia * aleatoriedade
            geracao_mensal += geracao_base_dia

        
        print(f"Geração em {mes_nome}: {geracao_mensal:.0f} kWh")
        geracao_anual.append(geracao_mensal)
        geracao_mensal = 0


soma_geracao = sum(geracao_anual)
media_geracao = soma_geracao / 12
print("Log de alertas:",alertas_log)
print("Total de alertas:",total_alertas)
#Vamos considerar que a geração esperada seja de 13.500 kWh
