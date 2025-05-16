# 21. Make a Custom Class Iterable
# Assignment:
# Create a class Countdown that takes a start number.
# Implement __iter__() and __next__() to
# make the object iterable in a for-loop, counting down to 0.

class Countdown:
    def __init__(self,start):
        self.current = start

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < 0:
            raise StopIteration
        else:
            current = self.current
            self.current -= 1
            return current
        
# Example usage:
# Create a Countdown object starting from 9
countdown: Countdown = Countdown(9)
print("countdown:")
for number in countdown:
    print(number)
    
