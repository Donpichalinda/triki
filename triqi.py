import random

def print_board(board):
    """Imprime el tablero de juego."""
    for row in board:
        print(" ".join(row))

def check_winner(board, player):
    """Verifica si un jugador ha ganado."""
    # ... (código para verificar ganador, similar al original)

def is_full(board):
    """Verifica si el tablero está lleno."""
    # ... (código para verificar si el tablero está lleno, similar al original)

def fill_randomly(board, difficulty):
    """Llena las casillas vacías del tablero de forma aleatoria, con diferentes niveles de dificultad."""
    players = ["X", "O"]
    while True:
        i = random.randint(0, 2)
        j = random.randint(0, 2)
        if board[i][j] == " ":
            # Evita victorias inmediatas del oponente
            if not check_winner(board, players[(players.index("X") + 1) % 2]):
                # Priorizar el centro si la dificultad es media o alta
                if difficulty > 0 and (i, j) not in [(1, 1)] and board[1][1] == " ":
                    continue
                board[i][j] = random.choice(players)
                break

def play(difficulty=1):
    """Juega una partida de tres en raya con un nivel de dificultad especificado."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]

    # Jugada inicial aleatoria entre las posibles victorias
    initial_moves = [(0, 0, 2, 2), (0, 2, 2, 0), (0, 1, 2, 1), (1, 0, 1, 2)]
    move = random.choice(initial_moves)
    board[move[0]][move[1]] = "X"
    board[move[2]][move[3]] = "X"

    fill_randomly(board, difficulty)

    print_board(board)

    if check_winner(board, "X"):
        print("¡Jugador X ganó!")
    elif is_full(board):
        print("¡Empate!") 

if __name__ == "__main__":
    difficulty = int(input("Ingrese el nivel de dificultad (0: fácil, 1: medio): "))
    play(difficulty)