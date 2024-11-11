# Lambda Function Example
square = lambda x: x ** 2
print("Square of 5:", square(5))  # Output: 25

# Decorator Example
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# Using the decorated function
say_hello()

# Generator Example
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

# Using the generator
print("Counting up to 5:")
for number in count_up_to(5):
    print(number)
