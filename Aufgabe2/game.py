import numpy as np
import constant

board = np.chararray((3, 3))
board[:] = ' '


def next_move(move, lplayer):
    if move == constant.WON:
        print(board.decode())
        return "game finished: [ {} ] has won".format(lplayer)
    if move == constant.TIE:
        print(board.decode())
        return "tie game"

    nplayer = constant.PLAYER_1 \
        if (lplayer == constant.PLAYER_2) \
        else constant.PLAYER_2

    x = np.random.randint(0, 9)
    check = check_if_boardentry_is_occupied(x)
    while check:
        x = np.random.randint(0, 9)
        check = check_if_boardentry_is_occupied(x)
        if not check:
            break

    index = map_board(x)
    row = index[0][0]
    col = index[1][0]
    board[row][col] = nplayer

    row = board[row][0:len(board):1]
    col = board[:, col]

    horizontal = np.all(row.decode() == nplayer)
    vertical = np.all(col.decode() == nplayer)
    diagonal = np.all(board.diagonal().decode() == nplayer)
    diagonal_left2right = np.all(np.fliplr(board).diagonal().decode() == nplayer)

    if horizontal or vertical or diagonal or diagonal_left2right:
        return next_move(constant.WON, nplayer)
    if check_if_game_is_draw():
        return next_move(constant.TIE, nplayer)
    return next_move(x, nplayer)


def map_board(position):
    labels = np.array([
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ])
    return np.where(labels == position)


def check_if_boardentry_is_occupied(position):
    index = map_board(position)
    if board[index[0][0]][index[1][0]]:
        return True
    return False


def check_if_game_is_draw():
    spaces = board.isspace()
    if True in spaces:
        return False
    return True


print(next_move(1, constant.PLAYER_2))
