# 15. Method Resolution Order (MRO) and Diamond Inheritance
# Assignment:
# Create four classes:

# A with a method show(),

# B and C that inherit from A and override show(),

# D that inherits from both B and C.

# Create an object of D and call show() to observe MRO.

class A:
    def show(self):
        print("A")

class B(A):
     def show(self):
        print("B")

class c(A):
     def show(self):
        print("C")

class D(B,c):
    pass
# Create an object of D and call show() to observe MRO.
d = D()
print(d.show())