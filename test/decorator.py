# Decorators are very powerful and useful tool in Python since it allows programmers to modify the
# behavior of function or class. Decorators allow us to wrap another function in order to extend the
# behavior of wrapped function, without permanently modifying it.
#
# In Decorators, functions are taken as the argument into another function and then
# called inside the wrapper function.

# back end working of decorator

def original_func():
    print( "\tHello...!!!")

def wrap_func(original_func):
    print(" modification code in the beginning of the function")
    original_func()
    print(" modification code in the beginning of the function")


wrap_func(original_func)

# How it is achieved :

def wrap_func(original_func):
    print(" modification code in the beginning of the function")
    original_func()
    print(" modification code in the beginning of the function")




@wrap_func
def original_func():
    print("\tHello...!!!")


