# 17. Class Decorators
# Assignment:
# Create a class decorator add_greeting that modifies a 
# class to add a greet() method returning "Hello from Decorator!". Apply it to a class Person.

def  add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

# Apply the class decorator to a class
@add_greeting
class Person:
    def __init__(self,name):
        self.name = name

# Create an instance of the decorated class
person:Person = Person("Harry")
print(person.greet())  # Output: Hello from Decorator!
print(person.name)  # Output: Harry

        
    
        

