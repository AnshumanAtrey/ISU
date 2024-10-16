import math

# ceil(x) - Returns the smallest integer greater than or equal to x.
def example_ceil():
    x = 4.2
    result = math.ceil(x)
    print(f"ceil({x}) = {result}")  # Output: 5

# fabs(x) - Returns the absolute value of x.
def example_fabs():
    x = -5.5
    result = math.fabs(x)
    print(f"fabs({x}) = {result}")  # Output: 5.5

# factorial(x) - Returns the factorial of x, an integer.
def example_factorial():
    x = 5
    result = math.factorial(x)
    print(f"factorial({x}) = {result}")  # Output: 120

# floor(x) - Returns the largest integer less than or equal to x.
def example_floor():
    x = 4.7
    result = math.floor(x)
    print(f"floor({x}) = {result}")  # Output: 4

# fmod(x, y) - Returns the remainder when x is divided by y.
def example_fmod():
    x, y = 5, 2
    result = math.fmod(x, y)
    print(f"fmod({x}, {y}) = {result}")  # Output: 1.0

# fsum(iterable) - Returns an accurate floating point sum of values in the iterable.
def example_fsum():
    iterable = [1.1, 2.2, 3.3]
    result = math.fsum(iterable)
    print(f"fsum({iterable}) = {result}")  # Output: 6.6

# exp(x) - Returns e raised to the power of x.
def example_exp():
    x = 1
    result = math.exp(x)
    print(f"exp({x}) = {result}")  # Output: 2.718281828459045

# trunc(x) - Returns the truncated integer value of x.
def example_trunc():
    x = 4.9
    result = math.trunc(x)
    print(f"trunc({x}) = {result}")  # Output: 4

# isinf(x) - Returns True if x is a positive or negative infinity.
def example_isinf():
    x = float('inf')
    result = math.isinf(x)
    print(f"isinf({x}) = {result}")  # Output: True

# log(x[, base]) - Returns the logarithm of x to the base base (defaults to e).
def example_log():
    x = 10
    result = math.log(x, 10)
    print(f"log({x}, 10) = {result}")  # Output: 1.0

# isfinite(x) - Returns True if x is neither an infinity nor a NaN (Not a Number).
def example_isfinite():
    x = float('nan')
    result = math.isfinite(x)
    print(f"isfinite({x}) = {result}")  # Output: False

# pow(x, y) - Returns the value of x raised to the power of y.
def example_pow():
    x, y = 2, 3
    result = math.pow(x, y)
    print(f"pow({x}, {y}) = {result}")  # Output: 8.0

# prod(iterable) - Returns the product of all the elements in an iterable.
def example_prod():
    iterable = [1, 2, 3, 4]
    result = math.prod(iterable)
    print(f"prod({iterable}) = {result}")  # Output: 24

# sqrt(x) - Returns the square root of x.
def example_sqrt():
    x = 16
    result = math.sqrt(x)
    print(f"sqrt({x}) = {result}")  # Output: 4.0

# Main function to demonstrate all math functions
def main():
    example_ceil()
    example_fabs()
    example_factorial()
    example_floor()
    example_fmod()
    example_fsum()
    example_exp()
    example_trunc()
    example_isinf()
    example_log()
    example_isfinite()
    example_pow()
    example_prod()
    example_sqrt()

if __name__ == "__main__":
    main()