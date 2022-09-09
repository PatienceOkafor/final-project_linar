#to import random module
from code import interact
import random
#to create a range of random numbers between 1 - 100

n = random.randrange(1,100)
# to take user input to enter a number

guess = int(input("enter any number:"))

while n != guess: # if n is not equals to the input guess
    # if guess is smaller than n
    if guess < n:
        print("numbers too low!")
        # to ask again for input
        guess = int(input("Enter number again:"))
        # if guess is greater than n
    elif guess > n:
        print("number too high!")
        # to again ask for the user input
        guess = int(input("Enter number again"))
        # if guess equals to n teminates the while loop
    else:
        break
print("You guessed right!!")
        
