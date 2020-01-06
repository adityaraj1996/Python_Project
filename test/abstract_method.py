# abstract method
# no need to instantiate base class
# it expects sub class to override this method
class Animal():
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotimplementedError('expecting subclass to implement this abstract method')


class Dog(Animal):
    # no need to initialize now

    def speak(self):
        return self.name + " barks"


class Cat(Animal):
    # no need to initialize now

    def speak(self):
        return self.name + " meow"


tom = Dog('tom')
pussy = Cat('pussy')

print(tom.speak())
print(pussy.speak())