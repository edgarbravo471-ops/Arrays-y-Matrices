# ---------------------------------------------------------
# SISTEMA: AGENDA TELEFÓNICA
# LENGUAJE: Python
# DESCRIPCIÓN:
# Programa que permite registrar, buscar y listar contactos
# usando Programación Orientada a Objetos y estructuras de datos.
# ---------------------------------------------------------

# -----------------------------
# CLASE CONTACTO (REGISTRO)
# -----------------------------
class Contacto:
    """
    Representa un registro de un contacto telefónico.
    """

    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def mostrar_datos(self):
        """
        Retorna los datos del contacto en formato legible.
        """
        return f"Nombre: {self.nombre} | Teléfono: {self.telefono} | Email: {self.email}"


# -----------------------------
# CLASE AGENDA (VECTOR)
# -----------------------------
class AgendaTelefonica:
    """
    Administra un vector (lista) de contactos.
    """

    def __init__(self):
        # Vector donde se almacenan los contactos
        self.contactos = []

    def agregar_contacto(self, nombre, telefono, email):
        """
        Agrega un nuevo contacto a la agenda.
        """
        contacto = Contacto(nombre, telefono, email)
        self.contactos.append(contacto)

    def buscar_contacto(self, nombre):
        """
        Busca un contacto por nombre.
        """
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                return contacto
        return None

    def listar_contactos(self):
        """
        Retorna la lista completa de contactos.
        """
        return self.contactos


# -----------------------------
# CLASE REPORTERÍA
# -----------------------------
class Reporteria:
    """
    Permite visualizar y consultar la estructura de datos.
    """

    @staticmethod
    def mostrar_contactos(contactos):
        """
        Muestra todos los contactos almacenados.
        """
        if not contactos:
            print("No existen contactos registrados.")
        else:
            print("\n--- LISTADO DE CONTACTOS ---")
            for contacto in contactos:
                print(contacto.mostrar_datos())


# -----------------------------
# FUNCIÓN MENÚ PRINCIPAL
# -----------------------------
def mostrar_menu():
    print("\n===== AGENDA TELEFÓNICA =====")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Listar contactos")
    print("4. Salir")


# -----------------------------
# PROGRAMA PRINCIPAL
# -----------------------------
def main():
    agenda = AgendaTelefonica()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese nombre: ")
            telefono = input("Ingrese teléfono: ")
            email = input("Ingrese email: ")
            agenda.agregar_contacto(nombre, telefono, email)
            print("Contacto agregado correctamente.")

        elif opcion == "2":
            nombre = input("Ingrese el nombre a buscar: ")
            contacto = agenda.buscar_contacto(nombre)
            if contacto:
                print("\nContacto encontrado:")
                print(contacto.mostrar_datos())
            else:
                print("Contacto no encontrado.")

        elif opcion == "3":
            Reporteria.mostrar_contactos(agenda.listar_contactos())

        elif opcion == "4":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


# -----------------------------
# EJECUCIÓN DEL PROGRAMA
# -----------------------------
if __name__ == "__main__":
    main()
