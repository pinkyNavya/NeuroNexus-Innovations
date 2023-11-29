import math
import random
board = [' ' for _ in range(9)]
def check_win(board, player):
    win_cases = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for case in win_cases:
        if board[case[0]] == board[case[1]] == board[case[2]] == player:
            return True
    return False
def check_draw(board):
    return ' ' not in board
def evaluate(board):
    if check_win(board, 'X'):
        return -10
    elif check_win(board, 'O'):
        return 10
    elif check_draw(board):
        return 0
    else:
        return None
def minimax(board, depth, is_maximizing_player):
    eval_board = evaluate(board)
    if eval_board is not None:
        return eval_board

    if is_maximizing_player:
        max_eval = -math.inf
        for i in range(len(board)):
            if board[i] == ' ':
                board[i] = 'O'
                eval = minimax(board, depth + 1, False)
                max_eval = max(max_eval, eval)
                board[i] = ' '
        return max_eval

    else:
        min_eval = math.inf
        for i in range(len(board)):
            if board[i] == ' ':
                board[i] = 'X'
                eval = minimax(board, depth + 1, True)
                min_eval = min(min_eval, eval)
                board[i] = ' '
        return min_eval
def make_move(board, player):
    best_move_index = None
    best_move_eval = -math.inf
    for i in range(len(board)):
        if board[i] == ' ':
            board[i] = player
            eval = minimax(board, 0, False)
            board[i] = ' '
            if eval > best_move_eval:
                best_move_eval = eval
                best_move_index = i
    board[best_move_index] = player
def play_game():
    print('Welcome to Tic-Tac-Toe!')
    print(' '.join(board))

    while not check_win(board, 'X') and not check_win(board, 'O') and not check_draw(board):
        human_move = input('Enter your move (1-9): ')
        while human_move not in map(str, range(1, 10)) or board[int(human_move) - 1] != ' ':
            human_move = input('Invalid move. Enter your move (1-9): ')
        human_move = int(human_move) - 1
        board[human_move] = 'X'
        print(' '.join(board))

        if not check_win(board, 'X') and not check_win(board, 'O') and not check_draw(board):
            make_move(board, 'O')
            print(' '.join(board))

    if check_win(board, 'X'):
        print('player wins!')
    elif check_win(board, 'O'):
        print('AI wins!')
    else:
        print('It\'s a draw!')

play_game()