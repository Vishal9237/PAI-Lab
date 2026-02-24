board = [" "] * 9

def print_board():
    print("\n")
    for i in range(3):
        print(f"{board[i*3]} | {board[i*3+1]} | {board[i*3+2]}")
        if i < 2:
            print("--+---+--")
    print("\n")

def check_winner():
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    
    for a,b,c in wins:
        if board[a] == board[b] == board[c] != " ":
            return board[a]
    
    if " " not in board:
        return "Draw"
    
    return None

def minimax(player):
    result = check_winner()
    if result == "O": return 1
    if result == "X": return -1
    if result == "Draw": return 0

    if player == "O":  
        best = -10
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                best = max(best, minimax("X"))
                board[i] = " "
        return best
    else:  
        best = 10
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                best = min(best, minimax("O"))
                board[i] = " "
        return best

def ai_move():
    best_val = -10
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            move_val = minimax("X")
            board[i] = " "
            if move_val > best_val:
                best_val = move_val
                move = i
    board[move] = "O"

def get_user_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            
            if move < 0 or move > 8:
                print("Please enter number between 1 and 9.")
            elif board[move] != " ":
                print("Position already taken. Try again.")
            else:
                return move
        except ValueError:
            print("Invalid input. Enter a number.")

print("Tic-Tac-Toe (You = X, AI = O)")
print("Positions are numbered 1 to 9 like this:")
print("1 | 2 | 3")
print("--+---+--")
print("4 | 5 | 6")
print("--+---+--")
print("7 | 8 | 9")

while True:
    print_board()
    
    move = get_user_move()
    board[move] = "X"
    
    if check_winner():
        break
    
    print("AI is thinking...")
    ai_move()
    
    if check_winner():
        break

print_board()
result = check_winner()

if result == "Draw":
    print("Game Draw!")
else:
    print(f"{result} wins!")
