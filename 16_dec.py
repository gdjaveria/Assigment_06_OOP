# 16. Function Decorators
# Assignment:
# Write a decorator function log_function_call that prints 
# "Function is being called" before a function executes. Apply it to a function say_hello().

def log_function_call(func):
    def wrapper(*args, **kwargs):
        print("Function is being called")
        return func(*args, **kwargs)
    return wrapper

# Apply the decorator to the function
@log_function_call
def say_hello():
    return"Hello, World!" # This will be printed after the decorator message

# Call the decorated function
print(say_hello())


    

