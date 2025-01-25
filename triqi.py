import random

def print_board(board):
    """Imprime el tablero de juego."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    """Verifica si un jugador ha ganado."""
    # Verificar filas y columnas
    for i in range(3):
        if all(cell == player for cell in board[i]):
            return True
        if all(row[i] == player for row in board):
            return True

    # Verificar diagonales
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_full(board):
    """Verifica si el tablero está lleno."""
    return all(cell != " " for row in board for cell in row)

def fill_randomly(board, current_player):
    """Llena una casilla vacía de forma aleatoria."""
    while True:
        i = random.randint(0, 2)
        j = random.randint(0, 2)
        if board[i][j] == " ":
            board[i][j] = current_player
            break

def play():
    """Juega una partida de tres en raya con selección de dificultad."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]

    # Elegir dificultad
    while True:
        try:
            difficulty = int(input("Seleccione la dificultad (0: Fácil, 1: Difícil): "))
            if difficulty in [0, 1]:
                break
            else:
                print("Por favor, ingrese 0 o 1.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese 0 o 1.")

    # Determinar el jugador inicial de forma aleatoria
    current_player = random.choice(players)
    print(f"El jugador inicial es: {current_player}\n")

    while not is_full(board):
        print_board(board)
        print(f"Turno de: {current_player}\n")

        if difficulty == 0 or current_player == "X":
            # Fácil: siempre jugadas aleatorias
            fill_randomly(board, current_player)
        else:
            # Difícil: tratar de bloquear al oponente si está a punto de ganar
            moved = False
            opponent = "X" if current_player == "O" else "O"

            # Buscar una jugada para bloquear al oponente
            for i in range(3):
                for j in range(3):
                    if board[i][j] == " ":
                        board[i][j] = opponent
                        if check_winner(board, opponent):
                            board[i][j] = current_player
                            moved = True
                            break
                        board[i][j] = " "
                if moved:
                    break

            # Si no se encontró una jugada de bloqueo, jugar aleatoriamente
            if not moved:
                fill_randomly(board, current_player)

        # Verificar si hay un ganador
        if check_winner(board, current_player):
            print_board(board)
            print(f"\n¡El jugador {current_player} ha ganado!\n")
            return

        # Cambiar de jugador
        current_player = "X" if current_player == "O" else "O"

    print_board(board)
    print("\n¡Es un empate!\n")

if __name__ == "__main__":
    play()