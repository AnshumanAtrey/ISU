from random import randint
LOW, HIGH = 1,10
secret_number = randint (LOW, HIGH)
while True:
    guess = int(input(f"Guess a number between {LOW} and {HIGH} : "))
    if guess > secret_number:
        print(f"Secret Number is less than {guess}")
    elif guess < secret_number:
        print(f"Secret Number is greater than {guess}")
    else:
        break
print(f"You guessed it! The secret Number is {guess}")