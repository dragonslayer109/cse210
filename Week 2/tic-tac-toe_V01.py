
def main():
    player1 = "X"
    player2 = "O"
    player1_ticket = 1
    player2_ticket = 0
    board = create_board()
    while not (winner(board) or draw(board)):
        display_board(board)
        if player1_ticket == 1:
            player = player1
            player1_ticket = 0
            prompt_move(player, board)
            player2_ticket = 1
        if player2_ticket == 1:
            player = player2
            player2_ticket = 0
            prompt_move(player, board)
            player1_ticket = 1            
    display_board(board)
    print("Good game. Thanks for playing!") 

def create_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

def display_board(board):
    print()
    print("{}|{}|{}".format(board[0], board[1], board[2] ))
    print('-+-+-')
    #tring something new I learnt that is similar to .format
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()

def draw():
    pass

def winner():
    pass

def prompt_move(player, board):
    pass

if __name__ == "__main__":
    main()