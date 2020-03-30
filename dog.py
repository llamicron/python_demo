# Define a class
# Named Dog
# Entends object, the most base type
class Dog(object):

    # this special method gets called when creating a new object
    def __init__(self, name, color):
        # Assign properties
        self.name = name
        self.color = color

    def bark(self, loudness):
        if loudness > 10:
            print(self.name + " says woof!")
        else:
            print(self.name + " says woof")


# This block is very common
# The contents of this if statement will only run if you
# run dog.py directly from the command line
# NOT if you import dog.py from another module
if __name__ == '__main__':
    dog = Dog("doug", "brown")
    dog.bark(5)
    dog.bark(15)
