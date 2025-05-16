# 20. Creating a Custom Exception
# Assignment:
# Create a custom exception InvalidAgeError. Write a function check_age(age) 
# that raises this exception if age < 18. Handle it with try...except.

class InvalidAgeError(Exception):
               pass

def check_age(age):
        if age < 18:
            raise InvalidAgeError("Age must be 18 or older.")
        else:
            print("Age is valid.")
    
try:
        result = check_age(15)
        print(result)
except InvalidAgeError as e:
        print(f"Exception caught: {e}")
    
try:
        result = check_age(20)
        print(result)
except InvalidAgeError as e:
        print(f"Exception caught: {e}")
        