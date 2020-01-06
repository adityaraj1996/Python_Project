# sometimes the objects over which we want to perform next()
# is not iterator fun , so we need to convert those object to generator
# using iter() and this is the way to perfrom next() func on normal func
# def name():
s = 'aditya'
for i in s:

    print(i)

# s = name()

# print(next(s))
# we will get this error:
#     next(s)
# TypeError: 'str' object is not an iterator

# converting non-iterartor to iterator
s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))