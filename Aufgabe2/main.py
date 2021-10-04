import numpy as np
import constant

board = np.zeros((3, 3))

def next_move(last, last_player):
    """
    Nimmt den letzten gesetzen Wert entgegen und generiert einen neuen
    Spielzug für den nächsten Spieler, wenn dieser Spieler das Spiel gewinnt,
    wird eine 9 zurückgegeben (constant.WON) ansonsten der neu besetzte Index.
    :param last_player: der letzte Spieler der am Zug war
    :param last: letzter gesetzter Index
    :return:
    """
    if last == constant.WON:
        show_board()
        winner = ""
        if last_player == constant.PLAYER_1:
            winner = "[X]"
        if last_player == constant.PLAYER_2:
            winner = "[O]"
        return "game finished: {} wins.".format(winner)

    current_player = constant.PLAYER_1 if (last_player == constant.PLAYER_2) else constant.PLAYER_2

    if last == constant.NO_MOVE:
        x = np.random.randint(0, 8)
        index = get_row_and_column(x)
        row = index[0][0]
        col = index[1][0]
        board[row][col] = current_player
        return next_move(x, current_player)

    x = np.random.randint(0, 8)
    check = check_board(x)
    while check:
        x = np.random.randint(0, 8)
        check = check_board(x)
        if check:
            break

    index = get_row_and_column(x)
    row = index[0][0]
    col = index[1][0]
    board[row][col] = current_player

    row = board[row][0:len(board):1]
    col = board[:, col]
    win = 3 * current_player

    if np.sum(row) == win or np.sum(col) == win:
        return next_move(constant.WON, current_player)
    return next_move(x, current_player)


def check_board(position):
    """
    Prüft ob eine übergeben Position im Board Array bereits belegt wurde oder nicht
    :param position: [0..8] Wert
    :return: (true or false) / true wenn belegt, false wenn nicht belegt
    """
    index = get_row_and_column(position)
    return board[index[0][0]][index[1][0]] > 0


def get_row_and_column(position):
    """
    Gibt die Index-Position eines Wertes (0..8) zurück.
    :param position: [0..8] Wert
    :return: (array[i], array[i])
    """
    labels = np.array([
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ])
    return np.where(labels == position)

def show_board():
    for j in range(len(board)):
        for i in range(len(board)):
            if board[j][i] == constant.PLAYER_1:
                print("X", end=" | ")
            if board[j][i] == constant.PLAYER_2:
                print("O", end=" | ")
            if board[j][i] == 0:
                print("-", end=" | ")
        print()


print(next_move(-1, constant.PLAYER_1))

