import random
answer=random.randint(1,100)
guess=int(input("Enter your guess: "))
while guess!=answer:
    if guess<answer:
        print("Too low")
    else:
        print("Too high")
    guess=int(input("Enter your guess: "))
print("Congratulations! You guessed the number correctly.")