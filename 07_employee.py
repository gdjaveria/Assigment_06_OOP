# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name # public variable
        self._salary = salary # protected variable
        self.__ssn = ssn # private variable

# Create an instance of Employee
emp = Employee("javeria", 50000, "123-45-6789")
print(emp.name)
print(emp._salary) # Accessing protected variable
# print(employee.__ssn) # This will raise an AttributeError because __ssn is private
print(emp._Employee__ssn) # Accessing private variable using name mangling

        

