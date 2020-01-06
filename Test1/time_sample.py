import timeit
a = int(input("enter the first number").strip())
b = int(input("enter the second number").strip())


def summation(c,d):
    return(c+d)

def subtraction(c,d):
    return(c-d)


begin = timeit.default_timer()
print(summation(a,b))
end = timeit.default_timer()
print("The calculation time was {}".format(end-begin))


