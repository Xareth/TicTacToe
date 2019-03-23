import ai
import random
historical_board = [[' '] * 9]


def change_player(player):
        if player == 'x':
            player = 'o'
        else:
            player = 'x'
        return player


def show_board(board):
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("- + - + - ")
    print(board[3], "|", board[4], "|", board[5])
    print("- + - + - ")
    print(board[6], "|", board[7], "|", board[8])
    print()


def player_move(board, player):
    global historical_board
    if player == 'x':
        choice = human_player_move(board)
    else:
        choice = ai.ai_player_move(board, historical_board)
    return choice


def human_player_move(board):
    tries = 100
    while tries > 0:
        try:
            choice = random.randrange(0, 10)
            print(choice)
            if 1 <= choice <= 9:
                if board[choice - 1] == ' ':
                    return choice - 1
                else:
                    raise ValueError
            else:
                raise ValueError
        except ValueError:
            print('wrong choice')
            tries -= 1


def win_condition(board, player):
    result = 'tie'
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] != ' ':
            result = 'win'
    for i in range(0,3):
        if board[i] == board[i + 3] == board[i + 6] != ' ':
            result = 'win'
    if board[0] == board[4] == board[8] != ' ':
        result = 'win'
    if board[2] == board[4] == board[6] != ' ':
        result = 'win'
    if result == 'win':
        print(f'You won player {player}')
        score_board(player)
        if player == 'o':
            ai.teach_win(historical_board)
        if player == 'x':
            ai.teach_lose(historical_board)
        return False
    for element in board:
        if element == ' ':
            return True
    return False


def score_board(player):
    new_score = []
    with open('score.txt', 'r') as f:
        for line in f:
            try:
                new_score.append(int(line))
            except ValueError:
                new_score.append(line.strip('\n'))
    new_score[1] += 1
    if player == 'o':
        new_score[3] += 1
    if player == 'x':
        new_score[5] += 1
    new_score[7] = new_score[3] / (new_score[3] + new_score[5])
    with open('score.txt', 'w') as f:
        f.writelines(new_score[0] + '\n')
        f.writelines(str(new_score[1]) + '\n')
        f.writelines(new_score[2] + '\n')
        f.writelines(str(new_score[3]) + '\n')
        f.writelines(new_score[4] + '\n')
        f.writelines(str(new_score[5]) + '\n')
        f.writelines(new_score[6] + '\n')
        f.writelines(str(new_score[7]) + '\n')


def main():
    board = [
        ' ', ' ', ' ',
        ' ', ' ', ' ',
        ' ', ' ', ' ',
    ]
    player = 'x'
    while True:
        choice = player_move(board, player)
        board[choice] = player
        historical_board.append(board.copy())
        historical_board[-2].append(str(choice))
        show_board(board)
        result = win_condition(board, player)
        if result:
            player = change_player(player)
        else:
            break


if __name__ == '__main__':
    while True:
        main()



