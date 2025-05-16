 # 9. Abstract Classes and Methods
# Assignment:
# Use the abc module to create an abstract class Shape with an abstract method 
# area(). Inherit a class Rectangle that implements area().




# Abstract classes are classes that cannot be instantiated and are meant to be

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod 
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width , height):
        self.width = width
        self.height = height

# Initialize the width and height of the rectangle
    def area(self):
        return self.width * self.height
    
# Create an instance of Rectangle
rect = Rectangle(3,7)
print(rect.area())

       
   

