# Dados de faturamento
faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

# Cálculo do total
total = sum(faturamento.values())

# Cálculo do percentual
percentuais = {estado: (valor / total) * 100 for estado, valor in faturamento.items()}

# Resultados
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")
