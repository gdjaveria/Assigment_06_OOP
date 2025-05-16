# 10. Instance Methods
# Assignment:
# Create a class Dog with instance variables name and breed.
#  Add an instance method bark() that prints a message including the dog's name.

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        
     # Instance method to make the dog bark
    def bark(self):
        print(f"{self.name} says woof! ")

# Create an instance of Dog
dog = Dog("Buddy", "Golden Retriever")
dog.bark()  # Call the bark method

