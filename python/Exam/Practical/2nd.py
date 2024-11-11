#Develop a number guessing game using loops and conditional statements
import random as r
answer=r.randint(0,10)
guess=int(input("Guess a number : "))
while guess!=answer:
    if guess<answer:
        guess=int(input("Bigger  : "))
    elif answer<guess:
        guess=int(input("Smaller  : "))
print("Yeehh :)")

