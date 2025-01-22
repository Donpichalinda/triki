def print_board(board):
    for row in board:
        print(" ".join(row))

def check_winner(board, player):
    # Revisar filas
    for row in board:
        if row.count(player) == 3:
            return True
    # Revisar columnas
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Revisar diagonales
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def play():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    while True:
        print_board(board)
        print(f"Jugador {players[turn % 2]}")
        row = int(input("Fila: "))
        col = int(input("Columna: "))

        if board[row][col] == " ":
            board[row][col] = players[turn % 2]
            if check_winner(board, players[turn % 2]):
                print_board(board)
                print(f"¡Jugador {players[turn % 2]} ganó!")
                break
            if is_full(board):
                print_board(board)
                print("¡Empate!")
                break
            turn += 1
        else:
            print("Casilla ocupada, intenta de nuevo.")

if __name__ == "__main__":
    play()
