from os import system


board = [['_' for _ in range(3)] for _ in range(3)]


def display_board(lst):
    # This is basically the system() from os library which takes cmd in ()
    system('cls')
    print('\n')
    for i in board:
        print(i)
    # print(lst[0] + '||' + lst[1] + '||' + lst[2])
    # print('_______')
    # print(lst[3] + '||' + lst[4] + '||' + lst[5])
    # print('_______')
    # print(lst[6] + '||' + lst[7] + '||' + lst[8])

display_board(board)