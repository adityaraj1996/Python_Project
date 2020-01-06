# ty and catch error exceptions

while True:
    try:
        x = int(input('enter the valid integer: ').strip())
        ans = (x * 25)/10
        print(f'the product is {ans}')
        break
    except ValueError:
        print('the entered integer is invalid...please try again')
    finally:
        print('the finally statement is executed anyways')


    print('execution after the exception is handled')


# def this_fails():
#     x = (1/0)
# try:
#     this_fails()
# except ZeroDivisionError as err:
#     print('the error has occurred in the function',err)








