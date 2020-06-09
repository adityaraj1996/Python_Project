# for understanding generators we need to understand next and iter function

def sample_gen():
    for x in range(3):
        yield x

# this returns the memory location of generator
print(sample_gen())

# next func()
# craeting instance of geneartor

g = sample_gen()
print(next(g))
# suspend and resume functionality
print(next(g))
print(next(g))
print(next(g))

 # output == 0
#             1

# at the end of the loop we will be getting error , stop iteration but in for loop we don't , because this error
# gets handled
# this is what happens at backend with for loop
