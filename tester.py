from main import show_board, score_board


board_string = ' xo     x0'
board = []
for i in range(len(board_string)):
    board.append(board_string[i])
show_board(board)

