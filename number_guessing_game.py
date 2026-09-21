import random 
print("""
Welcome to Number Guessing Game!
I have a number in mind, can you guess it? 
You only have 6 attempts. 
HINT: The number is between 1 - 20. 
Goodluck!!!
     """ )

secret_number = random.randint(1, 20)
count = 0

for num in range(6): 
    print("Guess my secret number.")
    guess = int(input())
    
    if guess > secret_number:
        print("Your guess is high, think of a lower number")
    elif guess < secret_number: 
        print("Your guess is low, the number is bigger")
    else: 
        break
    count +1

if guess == secret_number:
    print(f"You are right! The number is {secret_number}\n You got it in {count} counts")
else: 
    print(f"You run out of guesses! The number is {secret_number}")  