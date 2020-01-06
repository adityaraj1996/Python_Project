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

 # output == 0
#             1

# this is what happens at backend with for loop
