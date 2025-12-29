import math

board = [" " for _ in range(9)]

def print_for_board():
    print()
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("---------")
    print()

def check_for_winner(player):
    winning_conditions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    return any(all(board[i] == player for i in combo) for combo in winning_conditions)

def is_full():
    return " " not in board

def minimax(is_maximizing):
    if check_for_winner("O"):
        return 1
    if check_for_winner("X"):
        return -1
    if is_full():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(best_score, score)
        return best_score

def ai_chance():
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "O"

def play():
    print("Welcome to Tic-Tac-Toe. You are X and the AI- computer is O.")
    print_for_board()
    while True:
        move = int(input("Enter your move (1-9): ")) - 1
        if board[move] != " ":
            print("Try another")
            continue
        board[move] = "X"
        print_for_board()
        if check_for_winner("X"):
            print("You win")
            break
        if is_full():
            print("The game is a draw")
            break
        print("The computer is thinking...")
        ai_chance()
        print_for_board()
        if check_for_winner("O"):
            print("The computer wins")
            break
        if is_full():
            print("The game is a draw")
            break

play()
