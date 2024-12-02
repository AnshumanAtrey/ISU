import random

# randint(a, b) - Returns a random integer N such that a <= N <= b.
def example_randint():
    a, b = 1, 10
    result = random.randint(a, b)
    print(f"randint({a}, {b}) = {result}")

# randrange(start, stop[, step]) - Returns a randomly selected element from range(start, stop, step).
def example_randrange():
    start, stop, step = 1, 10, 2
    result = random.randrange(start, stop, step)
    print(f"randrange({start}, {stop}, {step}) = {result}")

# choice(seq) - Returns a random element from the nonempty sequence seq.
def example_choice():
    seq = [1, 2, 3, 4, 5]
    result = random.choice(seq)
    print(f"choice({seq}) = {result}")

# shuffle(x[, random]) - Shuffles the elements in list x in place.
def example_shuffle():
    x = [1, 2, 3, 4, 5]
    random.shuffle(x)
    print(f"shuffle({x}) = {x}")

# uniform(a, b) - Returns a random floating point number N such that a <= N <= b.
def example_uniform():
    a, b = 1.0, 10.0
    result = random.uniform(a, b)
    print(f"uniform({a}, {b}) = {result}")

# Main function to demonstrate all random functions
def main():
    example_randint()
    example_randrange()
    example_choice()
    example_shuffle()
    example_uniform()

if __name__ == "__main__":
    main()
