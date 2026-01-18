# Definición del nodo
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


# Definición de la lista enlazada
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.contador = 0

    # Insertar al final
    def insertar_final(self, dato):
        nuevo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self.contador += 1

    # Insertar al inicio
    def insertar_inicio(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
        self.contador += 1

    # Mostrar la lista
    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")


# Función para verificar si un número es primo
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True


# Función para verificar si un número es Armstrong
def es_armstrong(numero):
    digitos = str(numero)
    potencia = len(digitos)
    suma = sum(int(d) ** potencia for d in digitos)
    return suma == numero


# Programa principal
lista_primos = ListaEnlazada()
lista_armstrong = ListaEnlazada()

n = int(input("Ingrese la cantidad de números a evaluar: "))

for _ in range(n):
    num = int(input("Ingrese un número entero: "))

    if es_primo(num):
        lista_primos.insertar_final(num)

    if es_armstrong(num):
        lista_armstrong.insertar_inicio(num)

# a. Número de datos insertados en cada lista
print("\nCantidad de elementos en la lista de números primos:", lista_primos.contador)
print("Cantidad de elementos en la lista de números Armstrong:", lista_armstrong.contador)

# b. Mensaje indicando la lista con más elementos
if lista_primos.contador > lista_armstrong.contador:
    print("\nLa lista de números primos contiene más elementos.")
elif lista_primos.contador < lista_armstrong.contador:
    print("\nLa lista de números Armstrong contiene más elementos.")
else:
    print("\nAmbas listas contienen la misma cantidad de elementos.")

# c. Mostrar todos los datos insertados
print("\nLista de números primos (insertados al final):")
lista_primos.mostrar()

print("\nLista de números Armstrong (insertados al inicio):")
lista_armstrong.mostrar()
