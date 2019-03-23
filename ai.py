import random


def ai_player_move(board, historical):
    free_fields = find_free_fields(board)
    possible_wins = find_wins(board, free_fields)
    if possible_wins != []:
        choice = random.choice(possible_wins)
        print('I know how to win this game')
    else:
        possible_moves = find_loses(board, free_fields, historical)
        if possible_moves != []:
            choice = random.choice(possible_moves)
            print('I will use random value now, which I think i will not loose the match')
        else:
            choice = random.choice(find_free_fields(board))
            print('Nevermind... I lost')
            print(historical, 'this is printed historical board')
            teach_advance_lose(historical)
    return choice


def find_free_fields(board):
    free_fields = []
    for i in range(len(board)):
        if board[i] == ' ':
            free_fields.append(i)
    return free_fields


def find_wins(board, free_fields):
    current_board = ''.join(board)
    possible_wins = []
    with open('wins.csv') as f:
        for line in f:
            if line[:8] == current_board:
                if line[9] in free_fields:
                    possible_wins.append(line[9])
    return possible_wins


def teach_win(historical_board):
    wins = []
    with open('wins.csv', 'r') as f:
        for line in f:
            wins.append(line.strip('\n'))
    historic_result = ''.join(historical_board[-2])
    wins.append(historic_result)
    with open('wins.csv', 'w') as f:
        for element in wins:
            new_element = element + '\n'
            f.writelines(new_element)


def find_loses(board, free_fields, historical):
    dont_loose_list = free_fields
    print(dont_loose_list, 'these are my free fields')
    current_board = ''.join(board)
    with open('loses.csv', 'r') as f:
        for line in f:
            if line[:9] == current_board:
                if int(line[9]) in free_fields:
                    dont_loose_list.remove(int(line[9]))
                    print(dont_loose_list, f'I removed {line[9]}')
        print(f'These are the choices that are left. {dont_loose_list} I will use random number')
        if dont_loose_list != []:
            return dont_loose_list
        else:
            print('I lost... I will learn from this lesson')

            return free_fields


def teach_lose(historical_board):
    loses = []
    with open('loses.csv', 'r') as f:
        for line in f:
            loses.append(line.strip('\n'))
    historic_result = ''.join(historical_board[-3])
    print('xxxxxoooo1')
    print(historic_result)
    loses.append(historic_result)
    with open('loses.csv', 'w') as f:
        for element in loses:
            new_element = element + '\n'
            f.writelines(new_element)


def teach_advance_lose(historical_board):
    loses = []
    with open('loses.csv', 'r') as f:
        for line in f:
            loses.append(line.strip('\n'))
    historic_result = ''.join(historical_board[-3])
    historic_result = historic_result + ' this is advanced loss'
    loses.append(historic_result)
    with open('loses.csv', 'w') as f:
        for element in loses:
            new_element = element + '\n'
            f.writelines(new_element)
