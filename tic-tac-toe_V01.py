
def main():
    board = create_board()
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

if __name__ == "__main__":
    main()