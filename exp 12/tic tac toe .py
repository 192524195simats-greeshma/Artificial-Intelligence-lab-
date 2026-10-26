
def print_board(board):
    print("\n")
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print()


def check_winner(board, player):
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in wins:
        if board[a] == board[b] == board[c] == player:
            return True
    return False


def main():
    board = [" "] * 9
    player = "X"

    print("WELCOME TO TIC TAC TOE!")
    print("Choose a position from 1 to 9.")
    print(" 1 | 2 | 3")
    print("---+---+---")
    print(" 4 | 5 | 6")
    print("---+---+---")
    print(" 7 | 8 | 9")

    while True:
        print_board(board)

        try:
            move = int(input("Player " + player + ", enter position (1-9): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if move < 1 or move > 9:
            print("Choose a number between 1 and 9.")
            continue

        if board[move - 1] != " ":
            print("Position already taken! Try another.")
            continue

        board[move - 1] = player

        if check_winner(board, player):
            print_board(board)
            print("Player " + player + " wins! Congratulations!")
            break

        if " " not in board:
            print_board(board)
            print("It's a draw!")
            break

        player = "O" if player == "X" else "X"

    print("GAME OVER!")


if __name__ == "__main__":
    main()

    main()

