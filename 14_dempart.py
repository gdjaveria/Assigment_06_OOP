# 14. Aggregation
# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a 
# Department object store a reference to an Employee object that exists independently of it.

class Employee:
    def __init__(self,name,):
        self.name = name

class Department:
    def __init__(self,employee):
        self.employee = employee

# Create an instance of Employee and pass it to the Department class
Employee1 = Employee("zarnish")
dept = Department(Employee1)
print(dept.employee.name)
        

