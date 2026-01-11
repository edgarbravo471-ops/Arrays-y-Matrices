import math

# Pedir la muestra de números
entrada = input("Ingrese una muestra de números separados por comas: ")

# Convertir la entrada en una lista de números
numeros = [float(num) for num in entrada.split(",")]

# Calcular la media
media = sum(numeros) / len(numeros)

# Calcular la desviación típica
suma_cuadrados = 0
for num in numeros:
    suma_cuadrados += (num - media) ** 2

desviacion_tipica = math.sqrt(suma_cuadrados / len(numeros))

# Mostrar resultados
print(f"Media: {media}")
print(f"Desviación típica: {desviacion_tipica}")
