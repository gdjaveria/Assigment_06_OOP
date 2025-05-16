# 3. Public Variables and Methods
 # Assignment:
# Create a class Car with a public variable brand and a public method start(). 
# Instantiate the class and access both from outside the class.

class Car:
    def __init__(self):
        self.brand = "Toyota"

    def start (self):
        print(f"{self.brand} is starting.....")

# Create an instance of Car
my_car = Car()
print(my_car.brand)  # Accessing the public variable
my_car.start()  # Calling the public method

    