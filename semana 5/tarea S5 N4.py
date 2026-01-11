# Pedir una palabra al usuario
palabra = input("Ingrese una palabra: ").lower()

# Contadores de vocales
vocales = {
    "a": 0,
    "e": 0,
    "i": 0,
    "o": 0,
    "u": 0
}

# Contar las vocales
for letra in palabra:
    if letra in vocales:
        vocales[letra] += 1

# Mostrar resultados
print("Número de veces que aparece cada vocal:")
for vocal, cantidad in vocales.items():
    print(f"{vocal}: {cantidad}")
