def player_input():
    marker = ''
    # while marker != 'X' and marker != 'O':
    # to handle the case sensitivity
    while marker.lower() != 'x' and marker.lower() != 'o':
        #     while marker != 'X' and marker != 'O':
        marker = input("Player 1, enter 'X' or 'O'")
    player_1 = marker

    if player_1 == 'x':
        player_2 = 'o'
    else:
        player_2 = 'x'

    return (player_1, player_2)


print(player_input())
