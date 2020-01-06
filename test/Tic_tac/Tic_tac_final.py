def main():
    board = [['_' for _ in range(3)] for _ in range(3)]
    game_over = False
    is_x = True
    # display_board(board)
    while not game_over:
        display_board(board)
        try:
            selection = convert_selection(slct_position())
            place_marker(selection,is_x, board)
    # print(selection)

        except ValueError:
            print("please, enter a valid number between 1 and 9")
            # this is to prevent the missing turn if invalid value is entered
            continue

        # to see at the end of each turn if there is a draw
        game_over = is_draw(board) or is_win(board)

        # if game_over:
        #     display_board(board)
        #     print(" Ooops.....the game is drawn...!!!!")


        is_x = not is_x

        # display_board(board)

from os import system

# since , the selection is integer but the board is a matrix .
# so we need to convert selection to board index.
def convert_selection(selection):
    selection -= 1
    return(selection // 3,selection % 3)

def place_marker(selection,is_x,board):
    if board[selection[0]][selection[1]] == '_':
        board[selection[0]][selection[1]] = 'x' if is_x else 'o'
    else:
        print("sorry , the position is taken. Please try some other position")



def display_board(lst):
    # This is basically the system() from os library which takes cmd in ()
    # system('cls')
    print('\n')
    for i in lst:
        print(i)


def slct_position():
    position = int(input("Hey , enter the position you want to place marker at...from 1-9"))






    if not 1 <= position <= 9:
        raise ValueError
    return position

def is_draw(lst):
    for row in lst:
        for val in row:
            if val == "_":
                return False
    display_board(lst)
    print("Draw! No more moves!")
    # play_again = input("wanna play again ?...Enter yes or no..")
    # if play_again:

    return True

# def is_draw(lst):
#     flag = True
#     for i in lst:
#         for val in i:
#             if val == '_':
#                 flag = False
#     return flag

def is_win(lst):
    winner = None
    for i in range(3):





#  # horizontal Check
        if lst[i][0] == lst[i][1] == lst[i][2] and lst[i][0] != '_':
            winner = lst[i][0]

#  # vertical Check

        if lst[0][i] == lst[1][i] == lst[2][i] and lst[0][i] != '_':
            winner = lst[0][i]

#  # diaogonal Check

        if lst[1][1] != '_':
            if (lst[0][0] == lst[1][1] == lst[2][2]) or  (lst[0][2] == lst[1][1] == lst[2][0]):
                winner = lst[1][1]

    if winner is not None:

        display_board(lst)
        print(" congaratulations...!!! {} , you are the winner..!!!.".format(winner))
        return True
    return False



if __name__ == "__main__":
    main()


