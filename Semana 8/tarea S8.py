from collections import deque

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre


class Atraccion:
    def __init__(self, capacidad):
        self.capacidad_maxima = capacidad
        self.cola = deque()

    def llegar_persona(self, persona):
        self.cola.append(persona)
        print(f"{persona.nombre} ingresó a la fila.")

    def asignar_asientos(self):
        print("\nAsignando asientos...\n")
        asiento = 1

        while self.cola and asiento <= self.capacidad_maxima:
            persona = self.cola.popleft()
            print(f"Asiento {asiento} asignado a {persona.nombre}")
            asiento += 1

        if asiento > self.capacidad_maxima:
            print("\n🎢 Todos los asientos han sido vendidos. La atracción está llena.")


def main():
    atraccion = Atraccion(30)

    # Simulación de llegada de personas
    for i in range(1, 36):
        persona = Persona(f"Persona {i}")
        atraccion.llegar_persona(persona)

    atraccion.asignar_asientos()


if __name__ == "__main__":
    main()
