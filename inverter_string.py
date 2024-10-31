def inverter_string(s):
    string_invertida = ""
    for char in s:
        string_invertida = char + string_invertida
    return string_invertida

# Entrada do usuário
texto = input("Informe uma string: ")
print(f"String invertida: {inverter_string(texto)}")
