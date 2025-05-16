# 13. Composition
# Assignment:
# Create a class Engine and a class Car. Use composition by passing an 
# Engine object to the Car class during initialization. Access a method of the 
# Engine class via the Car class.

class Engine:
    def start_engine(self):
       print( "engine started")


class car:
    def __init__(self,engine):
        self.engine = engine

    def start_car(self):
        self.engine.start()
   
# Create an instance of Engine and pass it to the Car class
e = Engine()
c = car(e)
c.start_car()



