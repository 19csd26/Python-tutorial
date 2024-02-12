class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Cow(Animal):
    def make_sound(self):
        return "Moo!"

# Function to make animal sounds
def animal_sounds(animal):
    return animal.make_sound()

# Creating instances of different animals
dog = Dog()
cat = Cat()
cow = Cow()

# Polymorphic behavior
print(animal_sounds(dog))  # Output: Woof!
print(animal_sounds(cat))  # Output: Meow!
print(animal_sounds(cow))  # Output: Moo!

'''
In this example:

We have a base class Animal with a method make_sound(), which is overridden by subclasses Dog, Cat, and Cow.
The animal_sounds() function takes an object of type Animal (or any subclass of Animal) as a parameter and calls its make_sound() method.
When we pass different animal objects to the animal_sounds() function, polymorphism allows the correct make_sound() method of each object to be called based on its actual type.
Even though animal_sounds() function is only defined once, it behaves differently depending on the type of object passed to it, demonstrating polymorphic behavior.
'''
