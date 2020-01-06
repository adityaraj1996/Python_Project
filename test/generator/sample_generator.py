#code to understand the difference between normal function
#and generator

#normal function goes like this --
# we need to return the list of the cube of n(user input range) numbers

def cube(n):
    ans = []
    for i in range(n):
        ans.append(i**3)

    return ans

print(cube(8))

# ==> output is ==> [0, 1, 8, 27, 64, 125, 216, 343]

# using generator
#uses yiled keyword ,no need to store in a list which takes memory

def create_cube(n):
    for i in range(n):
        yield i**3

# below line will just display generator object created at some location
# if we want the list we have to cast it into list
print(create_cube(10))
print(list(create_cube(10)) )
