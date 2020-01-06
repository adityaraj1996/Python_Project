from os import system as sys


lst = [' '] * 9


def display_board(lst):
    sys('cls')
    print(lst[0] + '||' + lst[1] + '||' + lst[2])
    print('_______')
    print(lst[3] + '||' + lst[4] + '||' + lst[5])
    print('_______')
    print(lst[6] + '||' + lst[7] + '||' + lst[8])


def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input("Player 1, enter 'X' or 'O'")
    player_1 = marker

    if player_1 == 'X':
        player_2 = 'O'
    else:
        player_2 = 'X'

    return (player_1, player_2)


# defining the marker position on the board
def marker_pos(board_lst,position,marker):
    board_lst[position] = marker


marker_pos(lst, 2, 'X')
display_board(lst)
print(player_input())