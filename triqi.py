import random

def mostrar_tablero(tablero):
    for fila in tablero:
        print(" | ".join(fila))
    print()

def jugada_automatica(tablero):
    # Encuentra las posiciones vacías en el tablero
    posiciones_vacias = [(i, j) for i in range(3) for j in range(3) if tablero[i][j] == " "]
    if posiciones_vacias:
        # Elige una posición aleatoria vacía
        i, j = random.choice(posiciones_vacias)
        tablero[i][j] = "O"

# Inicializa el tablero vacío
tablero = [[" " for _ in range(3)] for _ in range(3)]

# Ejemplo: Realizamos una jugada automática
print("Tablero inicial:")
mostrar_tablero(tablero)

jugada_automatica(tablero)

print("Tablero después de la jugada automática:")
mostrar_tablero(tablero)
