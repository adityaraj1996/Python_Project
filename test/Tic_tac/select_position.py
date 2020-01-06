def slct_position():
    position = int(input("enter the position you want to place marker at...from 1-9"))
    if not 1 <= position <= 9:
        raise ValueError
    return position

while True:

    try:
        selection = slct_position()
        print(selection)

    except ValueError:
        print("print enter a valid number between 1 and 9")


