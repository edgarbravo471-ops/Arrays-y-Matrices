import tkinter as tk
from tkinter import messagebox


def registrar_estudiante():
    try:
        id_estudiante = int(entry_id.get())
        nombres = entry_nombres.get()
        apellidos = entry_apellidos.get()
        direccion = entry_direccion.get()

        telefonos = [
            entry_tel1.get(),
            entry_tel2.get(),
            entry_tel3.get()
        ]

        if not nombres or not apellidos or not direccion or "" in telefonos:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        resultado = (
            f"ID: {id_estudiante}\n"
            f"Nombres: {nombres}\n"
            f"Apellidos: {apellidos}\n"
            f"Dirección: {direccion}\n"
            f"Teléfonos:\n"
            f"  1) {telefonos[0]}\n"
            f"  2) {telefonos[1]}\n"
            f"  3) {telefonos[2]}"
        )

        messagebox.showinfo("Estudiante Registrado", resultado)

    except ValueError:
        messagebox.showerror("Error", "El ID debe ser un número")


# Ventana principal
ventana = tk.Tk()
ventana.title("Registro de Estudiante")
ventana.geometry("400x420")
ventana.resizable(False, False)

# Título
titulo = tk.Label(ventana, text="Registro de Estudiante", font=("Arial", 16, "bold"))
titulo.pack(pady=10)

# Contenedor
frame = tk.Frame(ventana)
frame.pack(pady=10)

# Campos
tk.Label(frame, text="ID:").grid(row=0, column=0, sticky="e", pady=5)
entry_id = tk.Entry(frame)
entry_id.grid(row=0, column=1)

tk.Label(frame, text="Nombres:").grid(row=1, column=0, sticky="e", pady=5)
entry_nombres = tk.Entry(frame)
entry_nombres.grid(row=1, column=1)

tk.Label(frame, text="Apellidos:").grid(row=2, column=0, sticky="e", pady=5)
entry_apellidos = tk.Entry(frame)
entry_apellidos.grid(row=2, column=1)

tk.Label(frame, text="Dirección:").grid(row=3, column=0, sticky="e", pady=5)
entry_direccion = tk.Entry(frame)
entry_direccion.grid(row=3, column=1)

tk.Label(frame, text="Teléfono 1:").grid(row=4, column=0, sticky="e", pady=5)
entry_tel1 = tk.Entry(frame)
entry_tel1.grid(row=4, column=1)

tk.Label(frame, text="Teléfono 2:").grid(row=5, column=0, sticky="e", pady=5)
entry_tel2 = tk.Entry(frame)
entry_tel2.grid(row=5, column=1)

tk.Label(frame, text="Teléfono 3:").grid(row=6, column=0, sticky="e", pady=5)
entry_tel3 = tk.Entry(frame)
entry_tel3.grid(row=6, column=1)

# Botón
btn_registrar = tk.Button(
    ventana,
    text="Registrar Estudiante",
    font=("Arial", 11, "bold"),
    bg="#2e86de",
    fg="white",
    command=registrar_estudiante
)
btn_registrar.pack(pady=20)

# Ejecutar app
ventana.mainloop()
