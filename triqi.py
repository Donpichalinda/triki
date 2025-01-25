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

def fill_randomly(board):
    """Llena las casillas vacías del tablero de forma aleatoria, evitando victorias anticipadas."""
    players = ["X", "O"]
    while True:
        i = random.randint(0, 2)
        j = random.randint(0, 2)
        if board[i][j] == " ":
            # Evita victorias inmediatas del oponente
            if not check_winner(board, players[(players.index("X") + 1) % 2]):
                board[i][j] = random.choice(players)
                break

def play():
    """Juega una partida de tres en raya."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    # Jugada predeterminada para 'X'
    board[0][0] = "X"
    board[1][1] = "X"
    board[2][2] = "X"

    fill_randomly(board)

    print_board(board)

    if check_winner(board, "X"):
        print("¡Jugador X ganó!")
    elif is_full(board):
        print("¡Empate!") 

if __name__ == "__main__":
    play()