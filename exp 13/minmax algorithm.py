
# Minimax Algorithm for Tic-Tac-Toe

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None


def minimax(board, is_maximizing):
    winner = check_winner(board)

    if winner == "O":
        return 1
    elif winner == "X":
        return -1
    elif all(cell != " " for row in board for cell in row):
        return 0

    if is_maximizing:
        best_score = -float("inf")

        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)

        return best_score

    else:
        best_score = float("inf")

        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)

        return best_score


def best_move(board):
    best_score = -float("inf")
    move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, False)
                board[i][j] = " "

                if score > best_score:
                    best_score = score
                    move = (i, j)

    return move


# Main Game
board = [[" " for _ in range(3)] for _ in range(3)]

print("TIC TAC TOE - MINIMAX ALGORITHM")
print("You are X, Computer is O")

while True:
    print_board(board)

    # Player move
    row = int(input("Enter row (0-2): "))
    col = int(input("Enter column (0-2): "))

    if not (0 <= row < 3 and 0 <= col < 3):
        print("Invalid position! Try again.")
        continue

    if board[row][col] != " ":
        print("Position already occupied! Try again.")
        continue

    board[row][col] = "X"

    if check_winner(board) == "X":
        print_board(board)
        print("You Win!")
        break

    if all(cell != " " for r in board for cell in r):
        print_board(board)
        print("Game Draw!")
        break

    # Computer move using Minimax
    move = best_move(board)

    if move:
        board[move[0]][move[1]] = "O"
        print("Computer played:", move)

    if check_winner(board) == "O":
        print_board(board)
        print("Computer Wins!")
        break

    if all(cell != " " for r in board for cell in r):
        print_board(board)
        print("Game Draw!")
        break
