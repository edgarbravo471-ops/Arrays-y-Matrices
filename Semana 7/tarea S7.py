def mover_disco(origen, destino):
    disco = origen.pop()
    destino.append(disco)

def torres_hanoi(n, origen, auxiliar, destino, nombre_origen, nombre_aux, nombre_destino):
    if n == 1:
        mover_disco(origen, destino)
        print(f"Mover disco 1 de {nombre_origen} a {nombre_destino}")
    else:
        torres_hanoi(n-1, origen, destino, auxiliar, nombre_origen, nombre_destino, nombre_aux)
        mover_disco(origen, destino)
        print(f"Mover disco {n} de {nombre_origen} a {nombre_destino}")
        torres_hanoi(n-1, auxiliar, origen, destino, nombre_aux, nombre_origen, nombre_destino)

# Número de discos
n = 3

# Pilas (torres)
origen = list(range(n, 0, -1))
auxiliar = []
destino = []

# Ejecución
torres_hanoi(n, origen, auxiliar, destino, "Origen", "Auxiliar", "Destino")
