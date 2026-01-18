import random

# Definición del nodo
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


# Definición de la lista enlazada
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    # Insertar nodo al final
    def insertar(self, dato):
        nuevo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    # Mostrar la lista
    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

    # Eliminar nodos fuera del rango
    def eliminar_fuera_rango(self, minimo, maximo):
        # Eliminar nodos iniciales fuera del rango
        while self.cabeza and (self.cabeza.dato < minimo or self.cabeza.dato > maximo):
            self.cabeza = self.cabeza.siguiente

        actual = self.cabeza
        while actual and actual.siguiente:
            if actual.siguiente.dato < minimo or actual.siguiente.dato > maximo:
                actual.siguiente = actual.siguiente.siguiente
            else:
                actual = actual.siguiente


# Programa principal
lista = ListaEnlazada()

# Crear la lista con 50 números aleatorios entre 1 y 999
for _ in range(50):
    lista.insertar(random.randint(1, 999))

print("Lista original:")
lista.mostrar()

# Leer rango desde teclado
minimo = int(input("Ingrese el valor mínimo del rango: "))
maximo = int(input("Ingrese el valor máximo del rango: "))

# Eliminar nodos fuera del rango
lista.eliminar_fuera_rango(minimo, maximo)

print("\nLista después de eliminar nodos fuera del rango:")
lista.mostrar()
