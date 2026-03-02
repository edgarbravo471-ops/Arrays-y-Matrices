import re

# Diccionario base inglés -> español
diccionario = {
    "time": "tiempo",
    "person": "persona",
    "year": "año",
    "way": "camino",
    "day": "día",
    "thing": "cosa",
    "man": "hombre",
    "world": "mundo",
    "life": "vida",
    "hand": "mano",
    "part": "parte",
    "child": "niño",
    "eye": "ojo",
    "woman": "mujer",
    "place": "lugar",
    "work": "trabajo",
    "week": "semana",
    "case": "caso",
    "point": "punto",
    "government": "gobierno",
    "company": "empresa"
}

def traducir_frase():
    frase = input("\nIngrese una frase: ")

    def traducir_palabra(match):
        palabra = match.group(0)
        palabra_lower = palabra.lower()
        if palabra_lower in diccionario:
            return diccionario[palabra_lower]
        return palabra

    traduccion = re.sub(r'\b\w+\b', traducir_palabra, frase)

    print("Traducción:")
    print(traduccion)

def agregar_palabra():
    ingles = input("\nIngrese la palabra en inglés: ").lower()
    espanol = input("Ingrese la traducción en español: ").lower()

    if ingles not in diccionario:
        diccionario[ingles] = espanol
        print("Palabra agregada correctamente.")
    else:
        print("La palabra ya existe en el diccionario.")

def menu():
    while True:
        print("\n==================== MENÚ ====================")
        print("1. Traducir una frase")
        print("2. Agregar palabras al diccionario")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            traducir_frase()
        elif opcion == "2":
            agregar_palabra()
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Programa principal
menu()