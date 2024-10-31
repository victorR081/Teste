import json

# Exemplo de dados em JSON
data = '''
{
    "faturamento": [1500.50, 2000.75, 0, 3000.00, 0, 2500.30, 4500.80]
}
'''

# Carregar dados do faturamento
faturamento = json.loads(data)["faturamento"]

# Ignorar dias sem faturamento
dias_com_faturamento = [valor for valor in faturamento if valor > 0]

# Cálculos
menor_faturamento = min(dias_com_faturamento)
maior_faturamento = max(dias_com_faturamento)
media_faturamento = sum(dias_com_faturamento) / len(dias_com_faturamento)
dias_acima_media = sum(1 for valor in dias_com_faturamento if valor > media_faturamento)

# Resultados
print(f"Menor faturamento: R${menor_faturamento:.2f}")
print(f"Maior faturamento: R${maior_faturamento:.2f}")
print(f"Número de dias acima da média: {dias_acima_media}")
