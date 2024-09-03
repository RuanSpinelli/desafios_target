import pandas as pd


#lendo o json com o faturamento diário
#indicando o endereço do json na minha máquina
df = pd.read_json('c:/Users/RUANN/OneDrive/Área de Trabalho/desafios target/3/faturamento.json')


df_faturamento = pd.json_normalize(df['faturamento_diario'])

#print(df_faturamento)

# Filtrar os dias com faturamento
df_faturamento_validos = df_faturamento[df_faturamento['valor'] > 0]

# Menor valor de faturamento
menor_valor = df_faturamento_validos['valor'].min()

# Maior valor de faturamento
maior_valor = df_faturamento_validos['valor'].max()

# Média mensal
media_mensal = df_faturamento_validos['valor'].mean()

# Número de dias com faturamento superior à média
dias_acima_media = df_faturamento_validos[df_faturamento_validos['valor'] > media_mensal].shape[0]

# Exibir os resultados
print(f"Menor valor de faturamento: R${menor_valor:.2f}")
print(f"Maior valor de faturamento: R${maior_valor:.2f}")
print(f"Número de dias com faturamento superior à média: {dias_acima_media} dias")
