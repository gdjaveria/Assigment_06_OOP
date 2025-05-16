 # 6. Constructors and Destructors
# Assignment:
# Create a class Logger that prints a message when an object is created (constructor)
#  and another message when it is destroyed (destructor).

class Logger:
    def __init__(self):
        print("Logger object is created.")
    
    def __del__(self):
        print("Logger object is destroyed.")

# Create an instance of Logger
my_Logger = Logger()
del my_Logger  # Explicitly delete the object to trigger the destructor


