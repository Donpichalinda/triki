import random

def mostrar_tablero(tablero):
    for fila in tablero:
        print(" | ".join(fila))
    print()

def partida_completa(tablero):
    # Alterna entre "X" y "O" para simular una partida
    turnos = ["X", "O"]
    posiciones_vacias = [(i, j) for i in range(3) for j in range(3)]
    random.shuffle(posiciones_vacias)  # Mezclamos las posiciones para simular jugadas aleatorias

    for turno, (i, j) in zip(turnos * 5, posiciones_vacias):  # 5 turnos por jugador (9 casillas en total)
        tablero[i][j] = turno

# Inicializa el tablero vacío
tablero = [[" " for _ in range(3)] for _ in range(3)]

# Simulamos una partida completa
partida_completa(tablero)

print("Tablero al final de una partida completa:")
mostrar_tablero(tablero)
