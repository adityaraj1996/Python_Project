class Animal():
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + " barks ")

# same method name used by diff class 
class Human(Animal):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + " says ")


new_Animal = Animal('dog')
new_Human = Human('jack')

new_Animal.speak()
new_Human.speak()
