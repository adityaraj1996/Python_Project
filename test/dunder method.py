# magic/dunder method

class Dog():

    def __init__(self, name, breed, lyf):
        self.name = name
        self.breed = breed
        self.lyf = lyf

    def __str__(self):
        return ("the dog's name is {} and breed is {} and the lyf is {}".format('tommy', 'lab', 8))


my_dog = Dog('Tommy', 'lab', 8)
# this print func will go to class Dog and ask for the str representation of my_dog , but we will not get what we
# want so , we will introduce a __str__ method to reslove this

print(my_dog)

