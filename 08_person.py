# 8. The super() Function
# Assignment:
# Create a class Person with a constructor that sets the name. 
# Inherit a class Teacher from it, add a subject field, and use super() 
# to call the base class constructor.

class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
        def __init__(self, name, subject):
            super().__init__(name) # Call the base class constructor
            self.subject = subject # Initialize the subject field

# Create an instance of Teacher
tech = Teacher("javeria", "Develpoer")
print(tech.name + " teaches " + tech.subject) # Accessing the name and subject fields

