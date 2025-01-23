def print_board(board):
    print("  0   1   2")
    for i, row in enumerate(board):
        print(i, " | ".join(row))
        if i < 2:
            print(" ---|---|--- ")

def check_winner(tablero, jugador):
    # Check rows
    for row in tablero:
        if all(s == jugador for s in row):
            return True

    # Check columns
    for col in range(3):
        if all(tablero[row][col] == jugador for row in range(3)):
            return True

    # Check diagonals
    if all(tablero[i][i] == jugador for i in range(3)) or all(tablero[i][2 - i] == jugador for i in range(3)):
        return True

    return False

def is_full(tablero):
    return all(all(cell != ' ' for cell in row) for row in tablero)

def juege():
    tablero = [[' ' for _ in range(3)] for _ in range(3)]
    jugadores = ['X', 'O']
    current_player = 0

    while True:
        print_board(tablero)
        row = int(input(f"Jugador {jugadores[current_player]}, ingresa la fila (0, 1, 2): "))
        col = int(input(f"Jugador {jugadores[current_player]}, ingresa la columna (0, 1, 2): "))

        if tablero[row][col] == ' ':
            tablero[row][col] = jugadores[current_player]
            if check_winner(tablero, jugadores=[current_player]):
                print_board(tablero)
                print(f"¡Jugador {jugadores[current_player]} ha ganado!")
                break
            elif is_full(tablero):
                print_board(tablero)
                print("¡Es un empate!")
                break
            current_player = 1 - current_player
        else:
            print("Esa posición ya está ocupada. Inténtalo de nuevo.")

if __name__ == "__main__":
    juege()
